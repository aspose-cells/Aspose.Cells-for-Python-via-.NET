import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "SmartMarkers" / "ImageMarkers"

def run():
    data_dir = get_data_dir()
    
    # Get the image data
    image_data1 = (data_dir / "aspose-logo.jpg").read_bytes()
    image_data2 = (data_dir / "image2.jpg").read_bytes()
    
    # Create WorkbookDesigner object
    designer = cells.WorkbookDesigner()
    # Open the template Excel file
    designer.workbook = cells.Workbook(str(data_dir / "TestSmartMarkers.xlsx"))
    
    # Set the datasource with image data list for marker name "Picture"
    designer.set_data_source("Picture", [image_data1, image_data2])
    # Process the markers
    designer.process()
    # Save the Excel file
    designer.workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    run()