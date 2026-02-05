import os
from pathlib import Path
from io import BytesIO
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "OLE" / "ExtractingOLEObjects"

def run_extracting_ole_objects():
    data_dir = str(get_data_dir())

    # Open the template file.
    workbook = cells.Workbook(os.path.join(data_dir, "book1.xls"))

    # Get the OleObject collection in the first worksheet.
    oles = workbook.worksheets[0].ole_objects

    # Loop through all the ole objects and extract each one.
    for i, ole in enumerate(oles):
        # Base output file name.
        file_name = os.path.join(data_dir, f"ole_{i}.")

        # Determine file extension based on the OleObject format type.
        fmt = ole.file_format_type
        if fmt == cells.FileFormatType.DOC:
            file_name += "doc"
        elif fmt == cells.FileFormatType.XLSX:
            file_name += "Xlsx"
        elif fmt == cells.FileFormatType.PPT:
            file_name += "Ppt"
        elif fmt == cells.FileFormatType.PDF:
            file_name += "Pdf"
        elif fmt == cells.FileFormatType.UNKNOWN:
            file_name += "Jpg"

        # Save the OleObject as a new Excel file if the object type is Xlsx.
        if fmt == cells.FileFormatType.XLSX:
            stream = BytesIO(bytearray(ole.object_data))
            ole_book = cells.Workbook(stream)
            ole_book.settings.is_hidden = False
            ole_book.save(os.path.join(data_dir, f"Excel_File{i}.out.xlsx"))
        else:
            # Save the raw OleObject data to a file.
            with open(file_name, "wb") as f:
                f.write(bytearray(ole.object_data))

if __name__ == "__main__":
    run_extracting_ole_objects()
