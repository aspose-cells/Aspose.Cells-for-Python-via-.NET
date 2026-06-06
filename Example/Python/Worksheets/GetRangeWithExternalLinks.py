import os
from pathlib import Path
from aspose.cells import Workbook, ReferredArea
from aspose.pydrawing import Color
from datetime import datetime

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    source_dir = get_source_directory()
    file_path = os.path.join(source_dir, "SampleExternalReferences.xlsx")
    
    workbook = Workbook(file_path)
    
    for named_range in workbook.worksheets.names:
        referred_areas = named_range.get_referred_areas(True)
        if referred_areas is not None:
            for referred_area in referred_areas:
                print(f"IsExternalLink: {referred_area.is_external_link}")
                print(f"IsArea: {referred_area.is_area}")
                print(f"SheetName: {referred_area.sheet_name}")
                print(f"ExternalFileName: {referred_area.external_file_name}")
                print(f"StartColumn: {referred_area.start_column}")
                print(f"StartRow: {referred_area.start_row}")
                print(f"EndColumn: {referred_area.end_column}")
                print(f"EndRow: {referred_area.end_row}")
    
    print("GetRangeWithExternalLinks executed successfully.\r\n")

if __name__ == "__main__":
    main()