import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Worksheets/Security/AdvancedProtectionSettings")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "02_OutputDirectory")

def main():
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    # Opening the Excel file
    excel = Workbook(os.path.join(data_dir, "book1.xls"))
    
    # Accessing the first worksheet in the Excel file
    worksheet = excel.worksheets[0]
    
    # Restricting users to delete columns of the worksheet
    worksheet.protection.allow_deleting_column = False
    
    # Restricting users to delete row of the worksheet
    worksheet.protection.allow_deleting_row = False
    
    # Restricting users to edit contents of the worksheet
    worksheet.protection.allow_editing_content = False
    
    # Restricting users to edit objects of the worksheet
    worksheet.protection.allow_editing_object = False
    
    # Restricting users to edit scenarios of the worksheet
    worksheet.protection.allow_editing_scenario = False
    
    # Restricting users to filter
    worksheet.protection.allow_filtering = False
    
    # Allowing users to format cells of the worksheet
    worksheet.protection.allow_formatting_cell = True
    
    # Allowing users to format rows of the worksheet
    worksheet.protection.allow_formatting_row = True
    
    # Allowing users to insert columns in the worksheet
    worksheet.protection.allow_formatting_column = True
    
    # Allowing users to insert hyperlinks in the worksheet
    worksheet.protection.allow_inserting_hyperlink = True
    
    # Allowing users to insert rows in the worksheet
    worksheet.protection.allow_inserting_row = True
    
    # Allowing users to select locked cells of the worksheet
    worksheet.protection.allow_selecting_locked_cell = True
    
    # Allowing users to select unlocked cells of the worksheet
    worksheet.protection.allow_selecting_unlocked_cell = True
    
    # Allowing users to sort
    worksheet.protection.allow_sorting = True
    
    # Allowing users to use pivot tables in the worksheet
    worksheet.protection.allow_using_pivot_table = True
    
    # Saving the modified Excel file
    output_path = os.path.join(get_output_directory(), "output.xls")
    excel.save(output_path, SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    main()