import os
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook, BorderType

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "Formatting/Excel2007Themes/CustomizeThemes")

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()
    
    # Define Color array (of 12 colors) for Theme.
    carr = [None] * 12
    carr[0] = drawing.Color.antique_white  # Background1
    carr[1] = drawing.Color.brown  # Text1
    carr[2] = drawing.Color.alice_blue  # Background2
    carr[3] = drawing.Color.yellow  # Text2
    carr[4] = drawing.Color.yellow_green  # Accent1
    carr[5] = drawing.Color.red  # Accent2
    carr[6] = drawing.Color.pink  # Accent3
    carr[7] = drawing.Color.purple  # Accent4
    carr[8] = drawing.Color.pale_green  # Accent5
    carr[9] = drawing.Color.orange  # Accent6
    carr[10] = drawing.Color.green  # Hyperlink
    carr[11] = drawing.Color.gray  # Followed Hyperlink

    # Instantiate a Workbook.
    # Open the template file.
    workbook = Workbook(os.path.join(data_dir, "book1.xlsx"))

    # Set the custom theme with specified colors.
    workbook.custom_theme("CustomeTheme1", carr)
    
    # Save as the excel file.
    workbook.save(os.path.join(data_dir, "output.out.xlsx"))
    # ExEnd:1

if __name__ == "__main__":
    run()