from datetime import datetime
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/UtilizeSheet_SheetId_PropertyOfOpenXml"

def main():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())

    # Load source Excel file
    wb = cells.Workbook(source_dir + "/sampleSheetId.xlsx")

    # Access first worksheet
    ws = wb.worksheets[0]

    # Print its Sheet or Tab Id on console
    print("Sheet or Tab Id: " + str(ws.tab_id))

    # Change Sheet or Tab Id
    ws.tab_id = 358

    # Save the workbook
    wb.save(output_dir + "/outputSheetId.xlsx")

    print("UtilizeSheet_SheetId_PropertyOfOpenXml executed successfully.\r\n")

if __name__ == "__main__":
    main()