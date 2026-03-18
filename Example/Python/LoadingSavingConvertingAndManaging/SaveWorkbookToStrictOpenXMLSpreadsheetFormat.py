import os
from aspose import pydrawing as drawing
import aspose.cells as cells
from aspose.cells import SaveFormat

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")

def main():
    output_dir = get_output_directory()
    
    # Create workbook
    wb = cells.Workbook()
    
    # Specify - Strict Open XML Spreadsheet - Format
    wb.settings.compliance = cells.OoxmlCompliance.ISO_29500_2008_STRICT
    
    # Add message in cell B4 of first worksheet
    worksheet = wb.worksheets[0]
    b4 = worksheet.cells.get("B4")
    b4.put_value("This Excel file has Strict Open XML Spreadsheet format.")
    
    # Save to output Excel file
    output_path = os.path.join(output_dir, "outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx")
    wb.save(output_path, SaveFormat.XLSX)
    
    print("SaveWorkbookToStrictOpenXMLSpreadsheetFormat executed successfully.")

if __name__ == "__main__":
    main()