import os
from datetime import datetime
from pathlib import Path
from aspose import pydrawing as drawing
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Security/AdvancedProtectionSettingsUsingAsposeCells"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Create output directory if it doesn't exist
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    # Opening the Excel file
    excel = cells.Workbook(str(data_dir / "book1.xls"))
    
    # Accessing the first worksheet
    worksheet = excel.worksheets[0]
    
    # Applying protection settings
    worksheet.protection.allow_deleting_column = False
    worksheet.protection.allow_deleting_row = False
    worksheet.protection.allow_editing_content = False
    worksheet.protection.allow_editing_object = False
    worksheet.protection.allow_editing_scenario = False
    worksheet.protection.allow_filtering = False
    worksheet.protection.allow_formatting_cell = True
    worksheet.protection.allow_formatting_row = True
    worksheet.protection.allow_formatting_column = True
    worksheet.protection.allow_inserting_hyperlink = True
    worksheet.protection.allow_inserting_row = True
    worksheet.protection.allow_selecting_locked_cell = True
    worksheet.protection.allow_selecting_unlocked_cell = True
    worksheet.protection.allow_sorting = True
    worksheet.protection.allow_using_pivot_table = True
    
    # Saving the file
    output_path = str(output_dir / "output.xls")
    excel.save(output_path, cells.SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()