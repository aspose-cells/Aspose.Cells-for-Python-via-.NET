import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, ConditionalFormattingResult
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/ComputeColorChoosenByMSExcel"

# Instantiate a workbook object
# Open the template file
data_dir = get_data_dir()
workbook = Workbook(str(data_dir / "Book1.xlsx"))

# Get the first worksheet
worksheet = workbook.worksheets[0]

# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()

# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read the color
print(c.to_argb())
print(c.name)