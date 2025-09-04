import logging
from io import BytesIO
from pathlib import Path
from typing import Any, Union, cast
import os

from docling_core.types.doc import (
    BoundingBox,
    CoordOrigin,
    DocItem,
    DoclingDocument,
    DocumentOrigin,
    GroupLabel,
    ImageRef,
    ProvenanceItem,
    Size,
    TableCell,
    TableData,
)
from aspose.cells import Workbook, WorksheetCollection, Worksheet
from aspose.cells.drawing import Picture
from PIL import Image as PILImage
from pydantic import BaseModel, NonNegativeInt, PositiveInt
from typing_extensions import override

from docling.backend.abstract_backend import (
    DeclarativeDocumentBackend,
    PaginatedDocumentBackend,
)
from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import InputDocument

_log = logging.getLogger(__name__)


# Example for Windows:
# PowerShell: $env:ASPOSE_LICENSE_PATH = "D:\Files\Aspose.Cells.lic"
# CMD:        set ASPOSE_LICENSE_PATH=D:\Files\Aspose.Cells.lic
class LicenseManager:
    def __init__(self):
        self.license_path = os.getenv("ASPOSE_LICENSE_PATH")

    def apply_license(self):
        from aspose.cells import License
        if self.license_path and os.path.exists(self.license_path):
            logging.info(f"Applying Aspose license from: {self.license_path}")
            lic = License()
            lic.set_license(self.license_path)
        else:
            logging.warning("=====> No valid Aspose license found. Running in free mode. Please set the ASPOSE_LICENSE_PATH environment variable!! <=====")


class ExcelCell(BaseModel):
    """Represents an Excel cell.

    Attributes:
        row: The row number of the cell.
        col: The column number of the cell.
        text: The text content of the cell.
        row_span: The number of rows the cell spans.
        col_span: The number of columns the cell spans.
    """

    row: int
    col: int
    text: str
    row_span: int
    col_span: int


class ExcelTable(BaseModel):
    """Represents an Excel table on a worksheet.

    Attributes:
        anchor: The column and row indices of the upper-left cell of the table
        (0-based index).
        num_rows: The number of rows in the table.
        num_cols: The number of columns in the table.
        data: The data in the table, represented as a list of ExcelCell objects.
    """

    anchor: tuple[NonNegativeInt, NonNegativeInt]
    num_rows: int
    num_cols: int
    data: list[ExcelCell]


class MsExcelDocumentBackend(DeclarativeDocumentBackend, PaginatedDocumentBackend):
    """Backend for parsing Excel workbooks.

    The backend converts an Excel workbook into a DoclingDocument object.
    Each worksheet is converted into a separate page.
    The following elements are parsed:
    - Cell contents, parsed as tables. If two groups of cells are disconnected
      from each other, they will be parsed as two different tables.
    - Images, parsed as PictureItem objects.

    The DoclingDocument tables and pictures have their provenance information, including
    the position in their original Excel worksheet. The position is represented by a
    bounding box object with the cell indices as units (0-based index). The size of this
    bounding box is the number of columns and rows that the table or picture spans.
    """

    @override
    def __init__(
        self, in_doc: "InputDocument", path_or_stream: Union[BytesIO, Path]
    ) -> None:
        """Initialize the MsExcelDocumentBackend object.

        Parameters:
            in_doc: The input document object.
            path_or_stream: The path or stream to the Excel file.

        Raises:
            RuntimeError: An error occurred parsing the file.
        """
        super().__init__(in_doc, path_or_stream)

        # Initialize the parent hierarchy
        self.max_levels = 10

        self.parents: dict[int, Any] = {}
        for i in range(-1, self.max_levels):
            self.parents[i] = None

        self.workbook = None
        try:
            LicenseManager().apply_license()
            if isinstance(self.path_or_stream, BytesIO):
                self.workbook = Workbook(self.path_or_stream)

            elif isinstance(self.path_or_stream, Path):
                self.workbook = Workbook(str(self.path_or_stream))
            
            self.valid = self.workbook is not None
        except Exception as e:
            self.valid = False
            raise RuntimeError(
                f"MsExcelDocumentBackend could not load document with hash {self.document_hash}"
            ) from e

    @override
    def is_valid(self) -> bool:
        _log.debug(f"valid: {self.valid}")
        return self.valid

    @classmethod
    @override
    def supports_pagination(cls) -> bool:
        return True

    @override
    def page_count(self) -> int:
        if self.is_valid() and self.workbook:
            return len(self.workbook.worksheets)
        else:
            return 0

    @classmethod
    @override
    def supported_formats(cls) -> set[InputFormat]:
        return {InputFormat.XLSX}

    @override
    def convert(self) -> DoclingDocument:
        """Parse the Excel workbook into a DoclingDocument object.

        Raises:
            RuntimeError: Unable to run the conversion since the backend object failed to
            initialize.

        Returns:
            The DoclingDocument object representing the Excel workbook.
        """
        
        origin = DocumentOrigin(
            filename=self.file.name or "file.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            binary_hash=self.document_hash,
        )

        doc = DoclingDocument(name=self.file.stem or "file.xlsx", origin=origin)

        if self.is_valid():
            doc = self._convert_workbook(doc)
        else:
            raise RuntimeError(
                f"Cannot convert doc with {self.document_hash} because the backend failed to init."
            )

        return doc

    def _convert_workbook(self, doc: DoclingDocument) -> DoclingDocument:
        """Parse the Excel workbook and attach its structure to a DoclingDocument.

        Args:
            doc: A DoclingDocument object.

        Returns:
            A DoclingDocument object with the parsed items.
        """
 
        if self.workbook is not None:
            # Iterate over all sheets
            for ws in self.workbook.worksheets:
                sheet_name = ws.name
                _log.info(f"Processing sheet: {sheet_name}")

                page_no = ws.index + 1
                page = doc.add_page(page_no=page_no, size=Size(width=0, height=0))

                self.parents[0] = doc.add_group(
                    parent=None,
                    label=GroupLabel.SECTION,
                    name=f"sheet: {sheet_name}",
                )
                doc = self._convert_sheet(doc, ws)
                width, height = self._find_page_size(doc, page_no)
                page.size = Size(width=width, height=height)
        else:
            _log.error("Workbook is not initialized.")

        return doc

    def _convert_sheet(self, doc: DoclingDocument, sheet: Worksheet) -> DoclingDocument:
        """Parse an Excel worksheet and attach its structure to a DoclingDocument.

        Args:
            doc: The DoclingDocument to be updated.
            sheet: The Excel worksheet to be parsed.

        Returns:
            The updated DoclingDocument.
        """
        doc = self._find_tables_in_sheet(doc, sheet)
        doc = self._find_images_in_sheet(doc, sheet)
        return doc

    def _find_tables_in_sheet(
        self, doc: DoclingDocument, sheet: Worksheet
    ) -> DoclingDocument:
        """Find all tables in an Excel sheet and attach them to a DoclingDocument.

        Args:
            doc: The DoclingDocument to be updated.
            sheet: The Excel worksheet to be parsed.

        Returns:
            The updated DoclingDocument.
        """

        if self.workbook is not None:
            tables = self._find_data_tables(sheet)

            for excel_table in tables:
                origin_col = excel_table.anchor[0]
                origin_row = excel_table.anchor[1]
                num_rows = excel_table.num_rows
                num_cols = excel_table.num_cols

                table_data = TableData(
                    num_rows=num_rows,
                    num_cols=num_cols,
                    table_cells=[],
                )

                for excel_cell in excel_table.data:
                    cell = TableCell(
                        text=excel_cell.text,
                        row_span=excel_cell.row_span,
                        col_span=excel_cell.col_span,
                        start_row_offset_idx=excel_cell.row,
                        end_row_offset_idx=excel_cell.row + excel_cell.row_span,
                        start_col_offset_idx=excel_cell.col,
                        end_col_offset_idx=excel_cell.col + excel_cell.col_span,
                        column_header=excel_cell.row == 0,
                        row_header=False,
                    )
                    table_data.table_cells.append(cell)

                page_no = sheet.index + 1
                doc.add_table(
                    data=table_data,
                    parent=self.parents[0],
                    prov=ProvenanceItem(
                        page_no=page_no,
                        charspan=(0, 0),
                        bbox=BoundingBox.from_tuple(
                            (
                                origin_col,
                                origin_row,
                                origin_col + num_cols,
                                origin_row + num_rows,
                            ),
                            origin=CoordOrigin.TOPLEFT,
                        ),
                    ),
                )

        return doc

    def _build_merged_lookup(self, areas):
        """
        areas: iterable of CellArea (from sheet.cells.get_merged_areas())  
        return: dict[(r,c)] -> CellArea
        """
        lookup = {}
        for a in areas:
            for r in range(a.start_row, a.end_row + 1):
                for c in range(a.start_column, a.end_column + 1):
                    lookup[(r, c)] = a
        return lookup

    def _get_bounds_from_area(self, area):
        """Compute (row_span, col_span) and (end_row, end_col) for a CellArea"""
        row_span = area.end_row - area.start_row + 1
        col_span = area.end_column - area.start_column + 1
        return row_span, col_span, area.end_row, area.end_column

    # -------------------- 1) Find table bottom --------------------
    def _find_table_bottom(self, sheet: Worksheet, start_row: int, start_col: int) -> int:
        """
        Equivalent to _find_table_bottom in openpyxl version:
        Starting from the row after (start_row, start_col), scan downward. 
        Stop when an empty cell (not in a merged area) is found.
        If inside a merged area, extend the bottom to the merged area's end_row.
        Note: Aspose uses 0-based indices.
        """
        max_row = start_row

        cells = sheet.cells
        last_row = cells.max_data_row if hasattr(cells, "max_data_row") else cells.max_row

        areas = list(cells.get_merged_areas() or [])
        merged_lookup = self._build_merged_lookup(areas)

        for ri in range(start_row + 1, last_row + 1):
            cell = cells.get(ri, start_col)
            area = merged_lookup.get((ri, start_col))

            if (cell is None or cell.value is None) and area is None:
                break

            if area is not None:
                _, _, end_r, _ = self._get_bounds_from_area(area)
                max_row = max(max_row, end_r)
            else:
                max_row = ri

        return max_row

    # -------------------- 2) Find table right --------------------
    def _find_table_right(self, sheet: Worksheet, start_row: int, start_col: int) -> int:
        """
        Equivalent to _find_table_right in openpyxl version:
        Scan to the right from the starting column. 
        Stop when an empty cell (not in a merged area) is found.
        If inside a merged area, extend to the merged area's end_column.
        """
        max_col = start_col

        cells = sheet.cells
        last_col = cells.max_data_column if hasattr(cells, "max_data_column") else cells.max_column

        areas = list(cells.get_merged_areas() or [])
        merged_lookup = self._build_merged_lookup(areas)

        for cj in range(start_col + 1, last_col + 1):
            cell = cells.get(start_row, cj)
            area = merged_lookup.get((start_row, cj))

            if (cell is None or cell.value is None) and area is None:
                break

            if area is not None:
                _, _, _, end_c = self._get_bounds_from_area(area)
                max_col = max(max_col, end_c)
            else:
                max_col = cj

        return max_col

    # -------------------- 3) Collect data + spans --------------------
    def _find_table_bounds(self, sheet: Worksheet, start_row: int, start_col: int):
        """
        Returns: (ExcelTable, visited_cells)
        Keeps the same structure as your existing version:
        Calculates (num_rows, num_cols) and each cell's row_span/col_span.
        """
        max_row = self._find_table_bottom(sheet, start_row, start_col)
        max_col = self._find_table_right(sheet, start_row, start_col)

        cells = sheet.cells
        areas = list(cells.get_merged_areas() or [])
        merged_lookup = self._build_merged_lookup(areas)

        visited_cells = set()
        data = []

        for ri in range(start_row, max_row + 1):
            for cj in range(start_col, max_col + 1):
                if (ri, cj) in visited_cells:
                    continue

                cell = cells.get(ri, cj)
                area = merged_lookup.get((ri, cj))
                if area is not None:
                    row_span, col_span, _, _ = self._get_bounds_from_area(area)
                else:
                    row_span, col_span = 1, 1

                data.append(
                    ExcelCell(
                        row=ri - start_row,
                        col=cj - start_col,
                        text="" if (cell is None or cell.value is None) else str(cell.value),
                        row_span=row_span,
                        col_span=col_span,
                    )
                )

                for r in range(ri, ri + row_span):
                    for c in range(cj, cj + col_span):
                        visited_cells.add((r, c))

        table = ExcelTable(
            anchor=(start_col, start_row),
            num_rows=max_row - start_row + 1,
            num_cols=max_col - start_col + 1,
            data=data,
        )
        return table, visited_cells

    def _find_data_tables(self, sheet: Worksheet) -> list:
        tables = []
        visited = set()

        cells = sheet.cells
        last_row = cells.max_data_row if hasattr(cells, "max_data_row") else cells.max_row
        last_col = cells.max_data_column if hasattr(cells, "max_data_column") else cells.max_column

        for ri in range(0, last_row + 1):
            for cj in range(0, last_col + 1):
                if (ri, cj) in visited:
                    continue
                cell = cells.get(ri, cj)
                if cell is None or cell.value is None:
                    continue

                table, used = self._find_table_bounds(sheet, ri, cj)
                visited.update(used)
                tables.append(table)

        return tables

    def _find_images_in_sheet(self, doc: DoclingDocument, sheet) -> DoclingDocument:
        """Find images in the Excel sheet and attach them to the DoclingDocument."""

        if self.workbook is not None:
            try:
                pictures = sheet.pictures
                page_no = sheet.index + 1

                for pic in pictures:  # type: Picture
                    img_bytes = pic.data
                    pil_image = PILImage.open(BytesIO(img_bytes))

                    anchor = (
                        pic.upper_left_column,
                        pic.upper_left_row,
                        pic.lower_right_column + 1,
                        pic.lower_right_row + 1,
                    )

                    doc.add_picture(
                        parent=self.parents[0],
                        image=ImageRef.from_pil(image=pil_image, dpi=72),
                        caption=None,
                        prov=ProvenanceItem(
                            page_no=page_no,
                            charspan=(0, 0),
                            bbox=BoundingBox.from_tuple(
                                anchor, origin=CoordOrigin.TOPLEFT
                            ),
                        ),
                    )
            except Exception as e:
                _log.error(f"could not extract the image from excel sheets: {e}")

        return doc

    @staticmethod
    def _find_page_size(
        doc: DoclingDocument, page_no: PositiveInt
    ) -> tuple[float, float]:
        left: float = -1.0
        top: float = -1.0
        right: float = -1.0
        bottom: float = -1.0
        for item, _ in doc.iterate_items(traverse_pictures=True, page_no=page_no):
            if not isinstance(item, DocItem):
                continue
            for provenance in item.prov:
                bbox = provenance.bbox
                left = min(left, bbox.l) if left != -1 else bbox.l
                right = max(right, bbox.r) if right != -1 else bbox.r
                top = min(top, bbox.t) if top != -1 else bbox.t
                bottom = max(bottom, bbox.b) if bottom != -1 else bbox.b

        return (right - left, bottom - top)
