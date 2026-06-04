import io
import matplotlib.pyplot as plt

from aspose.cells import Workbook
from aspose.cells.drawing import PlacementType

# --------------------------
# Step 1: Open Excel file
# --------------------------

workbook = Workbook("input.xlsx")
sheet = workbook.worksheets[0]

# --------------------------
# Step 2: Read data from Excel
# --------------------------

x = []
y = []

row = 1  # 假设第1行是标题

while True:
    x_value = sheet.cells.get(row, 0).value  # Column A
    y_value = sheet.cells.get(row, 1).value  # Column B

    if x_value is None:
        break

    x.append(x_value)
    y.append(y_value)

    row += 1

print("X =", x)
print("Y =", y)

# --------------------------
# Step 3: Generate chart using Matplotlib
# --------------------------

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker="o")

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

img_stream = io.BytesIO()
plt.savefig(img_stream, format="png", dpi=120)
plt.show()
plt.close()

img_stream.seek(0)

# --------------------------
# Step 4: Insert image into Excel
# --------------------------

pictures = sheet.pictures

index = pictures.add(2, 4, img_stream)
pic = pictures[index]

pic.placement = PlacementType.MOVE

# --------------------------
# Step 5: Save workbook
# --------------------------

workbook.save("output.xlsx")

print("Created: output.xlsx")