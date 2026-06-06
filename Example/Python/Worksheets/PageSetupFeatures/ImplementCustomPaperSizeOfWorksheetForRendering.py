import os
from pathlib import Path
import aspose.cells as cells

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    output_dir = get_output_directory()
    
    # Create output directory if it doesn't exist
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    # Create workbook object
    wb = cells.Workbook()
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Set custom paper size in unit of inches (Aspose.Cells for Python uses centimeters by default)
    # Convert inches to centimeters: 1 inch = 2.54 cm
    width_cm = 6 * 2.54
    height_cm = 4 * 2.54
    ws.page_setup.custom_paper_size(width_cm, height_cm)
    
    # Access cell B4
    b4 = ws.cells.get("B4")
    
    # Add the message in cell B4
    b4.put_value("Pdf Page Dimensions: 6.00 x 4.00 in")
    
    # Save the workbook in pdf format
    output_path = os.path.join(output_dir, "outputCustomPaperSize.pdf")
    wb.save(output_path)

if __name__ == "__main__":
    main()