import os
import tempfile
import logging

from marker.providers.pdf import PdfProvider

css = '''
@page {
    size: A4 landscape;
    margin: 1.5cm;
}

table {
    width: 100%;
    border-collapse: collapse;
    break-inside: auto;
    font-size: 10pt;
}

tr {
    break-inside: avoid;
    page-break-inside: avoid;
}

td {
    border: 0.75pt solid #000;
    padding: 6pt;
}
'''

# E,g. for Windows:
# PowerShell: $env:ASPOSE_LICENSE_PATH = "D:\Files\Aspose.Cells.lic"
# CDM:        set ASPOSE_LICENSE_PATH=D:\Files\Aspose.Cells.lic
class LicenseManager:
    def __init__(self):
        self.license_path = os.getenv("ASPOSE_LICENSE_PATH")

    def apply_license(self):
        # logging.warning(self.license_path)
        from aspose.cells import License
        if self.license_path and os.path.exists(self.license_path):
            logging.info(f"Applying Aspose license from: {self.license_path}")
            lic = License()
            lic.set_license(self.license_path)

        else:
            logging.warning("=====> No valid Aspose license found.Running in free mode.Please set the ASPOSE_LICENSE_PATH environment variable!! <=====")


class SpreadSheetProvider(PdfProvider):
    def __init__(self, filepath: str, config=None):
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=f".pdf")
        self.temp_pdf_path = temp_pdf.name
        temp_pdf.close()

        # Convert XLSX to PDF
        try:
            self.convert_xlsx_to_pdf(filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to convert {filepath} to PDF: {e}")

        # Initialize the PDF provider with the temp pdf path
        super().__init__(self.temp_pdf_path, config)

    def __del__(self):
        if os.path.exists(self.temp_pdf_path):
            os.remove(self.temp_pdf_path)

    def convert_xlsx_to_pdf(self, filepath: str):
        from weasyprint import CSS, HTML
        from aspose.cells import Workbook
        LicenseManager().apply_license()

        html = ""
        workbook = Workbook(filepath)
        workbook.save(filepath)
        workbook = Workbook(filepath)
        if workbook is not None:
            for ws in workbook.worksheets:
                sheet_name = ws.name
                # print("====" + sheet_name+ "=====")
                html += f'<div><h1>{sheet_name}</h1>' + self._excel_to_html_table(ws) + '</div>'
        else:
            raise ValueError("Invalid XLSX file")

        # We convert the HTML into a PDF
        HTML(string=html).write_pdf(
            self.temp_pdf_path,
            stylesheets=[CSS(string=css), self.get_font_css()]
        )

    @staticmethod
    def _get_merged_cell_ranges(sheet):
        merged_info = {}
        for area in sheet.cells.merged_cells:
            min_row, min_col = area.start_row + 1, area.start_column + 1
            max_row, max_col = area.end_row + 1, area.end_column + 1

            merged_info[(min_row, min_col)] = {
                'rowspan': max_row - min_row + 1,
                'colspan': max_col - min_col + 1,
                'range': area
            }
        return merged_info

    def _excel_to_html_table(self, sheet):
        # print("====_excel_to_html_table -- 1 ====")
        merged_cells = self._get_merged_cell_ranges(sheet)
        # print(merged_cells)
        html = f'<table>'

        skip_cells = set()

        max_row = sheet.cells.max_data_row + 1   #
        max_col = sheet.cells.max_data_column + 1

        for row_idx in range(max_row):
            html += '<tr>'
            for col_idx in range(max_col):
                key = (row_idx + 1, col_idx + 1)
                if key in skip_cells:
                    continue

                cell = sheet.cells.get(row_idx, col_idx)

                merge_info = merged_cells.get(key)
                if merge_info:
                    for r in range(row_idx + 1, row_idx + 1 + merge_info['rowspan']):
                        for c in range(col_idx + 1, col_idx + 1 + merge_info['colspan']):
                            if (r, c) != key:
                                skip_cells.add((r, c))

                    value = cell.value if cell.value is not None else ''
                    html += f'<td rowspan="{merge_info["rowspan"]}" colspan="{merge_info["colspan"]}">{value}'
                else:
                    value = cell.value if cell.value is not None else ''
                    html += f'<td>{value}'

                html += '</td>'
            html += '</tr>'

        html += '</table>'
        return html
 