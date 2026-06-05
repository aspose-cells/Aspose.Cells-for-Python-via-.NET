from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/DisplayHideScrollBars"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    
    # Creating a file stream containing the Excel file to be opened
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    # Instantiating a Workbook object
    # Opening the Excel file through the file stream
    workbook = Workbook(fstream)
    
    # Hiding the vertical scroll bar of the Excel file
    workbook.settings.is_v_scroll_bar_visible = False
    
    # Hiding the horizontal scroll bar of the Excel file
    workbook.settings.is_h_scroll_bar_visible = False
    
    # Saving the modified Excel file
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    workbook.save(os.path.join(output_dir, "output.xls"))
    
    # Closing the file stream to free all resources
    fstream.close()

if __name__ == "__main__":
    main()