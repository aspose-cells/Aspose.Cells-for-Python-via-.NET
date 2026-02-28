import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat, BackgroundType, BorderType
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/ColorsAndBackground"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Instantiating a Workbook object
    workbook = Workbook()

    # Adding a new worksheet to the Workbook object
    i = workbook.worksheets.add()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]

    # Define a Style and get the A1 cell style
    style = worksheet.cells.get("A1").get_style()

    # Setting the foreground color to yellow
    style.foreground_color = drawing.Color.yellow

    # Setting the background pattern to vertical stripe
    style.pattern = BackgroundType.VERTICAL_STRIPE

    # Apply the style to A1 cell
    worksheet.cells.get("A1").set_style(style)

    # Get the A2 cell style
    style = worksheet.cells.get("A2").get_style()

    # Setting the foreground color to blue
    style.foreground_color = drawing.Color.blue

    # Setting the background color to yellow
    style.background_color = drawing.Color.yellow

    # Setting the background pattern to vertical stripe
    style.pattern = BackgroundType.VERTICAL_STRIPE

    # Apply the style to A2 cell
    worksheet.cells.get("A2").set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

if __name__ == "__main__":
    run()