from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook()
# Obtaining the reference of the newly added worksheet
sheet = workbook.worksheets[0]
cells = sheet.cells
# Setting the value to the cells
cells.get("A1").put_value("First name")
cells.get("A2").put_value("Simon")
cells.get("A3").put_value("Kevin")
cells.get("A4").put_value("Leo")
cells.get("A5").put_value("Johnson")

cells.get("B1").put_value("Age")
cells.get("B2").put_value(32)
cells.get("B3").put_value(33)
cells.get("B4").put_value(34)
cells.get("B5").put_value(35)

cells.get("C1").put_value("Value")
cells.get("C2").put_value(123.546)
cells.get("C3").put_value(56.78)
cells.get("C4").put_value(34)
cells.get("C5").put_value(9)
# Saving the Excel file to json
workbook.save("JSON.json")