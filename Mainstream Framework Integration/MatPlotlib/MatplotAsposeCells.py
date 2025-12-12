# -*- coding: utf-8 -*-
"""
Demo: Combine Matplotlib and Aspose.Cells for Python via .NET
to insert a Matplotlib chart image into an Excel workbook.

Required packages:
    pip install matplotlib aspose-cells-python
"""

import os
from io import BytesIO

import matplotlib.pyplot as plt
from aspose.cells import Workbook, SaveFormat  # <-- note the import style


# ----------------------------------------------------------------------
# Step 1: Prepare data
# ----------------------------------------------------------------------
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# ----------------------------------------------------------------------
# Step 2: Create Matplotlib figure
# ----------------------------------------------------------------------
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-')
plt.title("Example Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# ----------------------------------------------------------------------
# Step 3: Save chart to memory as PNG
# ----------------------------------------------------------------------
img_stream = BytesIO()
plt.savefig(img_stream, format='png', bbox_inches='tight')
plt.close()               # close the figure ¨C we no longer need it
img_stream.seek(0)        # rewind the stream so Aspose.Cells can read it

# ----------------------------------------------------------------------
# Step 4: Insert the image (Matplotlib chart) using Aspose.Cells
# ----------------------------------------------------------------------
# Create a new workbook (or you could load an existing one)
workbook = Workbook()
worksheet = workbook.worksheets[0]   # get the first worksheet

# Add picture at row 2, column 2 (zero?based indices)
# Row 2 => third row, Column 2 => third column in Excel terms
worksheet.pictures.add(2, 2, img_stream)

# ----------------------------------------------------------------------
# Step 5: Save Excel file
# ----------------------------------------------------------------------
output_dir = r"D:\Git\Agent\AITestFile"
os.makedirs(output_dir, exist_ok=True)          # create folder if it does not exist
output_path = os.path.join(output_dir, "MatPlotlibAspose.xlsx")

workbook.save(output_path, SaveFormat.XLSX)

print(f"Excel file saved to: {output_path}")