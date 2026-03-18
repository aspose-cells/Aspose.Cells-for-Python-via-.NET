import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    source_dir = get_source_directory()
    
    load_options = cells.LoadOptions(cells.LoadFormat.CSV)
    workbook = cells.Workbook(str(source_dir / "SampleCsv.csv"), load_options)
    worksheet = workbook.worksheets[0]
    last_cell = worksheet.cells.last_cell
    
    range_obj = worksheet.cells.create_range(0, 0, last_cell.row + 1, last_cell.column + 1)
    data = cells.utility.JsonUtility.export_range_to_json(range_obj, cells.utility.ExportRangeToJsonOptions())
    
    print(data)
    print("ConvertCsvToJson executed successfully.")

if __name__ == "__main__":
    main()