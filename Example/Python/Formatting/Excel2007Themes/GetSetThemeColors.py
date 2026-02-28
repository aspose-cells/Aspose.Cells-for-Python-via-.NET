import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook, ThemeColorType
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting" / "Excel2007Themes" / "GetSetThemeColors"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Instantiate Workbook object.
    # Open an exiting excel file.
    workbook = Workbook(str(data_dir / "book1.xlsx"))

    # Get the Background1 theme color.
    c = workbook.get_theme_color(ThemeColorType.BACKGROUND1)

    # Print the color.
    print("theme color Background1: " + str(c))

    # Get the Accent2 theme color.
    c = workbook.get_theme_color(ThemeColorType.ACCENT2)

    # Print the color.
    print("theme color Accent2: " + str(c))

    # Change the Background1 theme color.
    workbook.set_theme_color(ThemeColorType.BACKGROUND1, Color.red)

    # Get the updated Background1 theme color.
    c = workbook.get_theme_color(ThemeColorType.BACKGROUND1)

    # Print the updated color for confirmation.
    print("theme color Background1 changed to: " + str(c))

    # Change the Accent2 theme color.
    workbook.set_theme_color(ThemeColorType.ACCENT2, Color.blue)

    # Get the updated Accent2 theme color.
    c = workbook.get_theme_color(ThemeColorType.ACCENT2)

    # Print the updated color for confirmation.
    print("theme color Accent2 changed to: " + str(c))

    # Save the updated file.
    workbook.save(str(data_dir / "output.out.xlsx"))
    # ExEnd:1

if __name__ == "__main__":
    run()