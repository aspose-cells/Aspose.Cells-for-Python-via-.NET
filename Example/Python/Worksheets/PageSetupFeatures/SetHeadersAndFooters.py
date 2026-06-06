import os
from datetime import datetime
from aspose.cells import Workbook, PageSetup
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Worksheets", "PageSetupFeatures", "SetHeadersAndFooters")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "02_OutputDirectory")

def run():
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    excel = Workbook()
    
    # Obtaining the reference of the PageSetup of the worksheet
    page_setup = excel.worksheets[0].page_setup
    
    # Setting worksheet name at the left section of the header
    page_setup.set_header(0, "&A")
    
    # Setting current date and current time at the central section of the header
    # and changing the font of the header
    page_setup.set_header(1, "&\"Times New Roman,Bold\"&D-&T")
    
    # Setting current file name at the right section of the header and changing the
    # font of the header
    page_setup.set_header(2, "&\"Times New Roman,Bold\"&12&F")
    
    # Setting a string at the left section of the footer and changing the font
    # of a part of this string ("123")
    page_setup.set_footer(0, "Hello World! &\"Courier New\"&14 123")
    
    # Setting the current page number at the central section of the footer
    page_setup.set_footer(1, "&P")
    
    # Setting page count at the right section of footer
    page_setup.set_footer(2, "&N")
    
    # Save the Workbook.
    output_path = os.path.join(get_output_directory(), "SetHeadersAndFooters_out.xls")
    excel.save(output_path)

if __name__ == "__main__":
    run()