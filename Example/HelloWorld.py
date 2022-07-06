import aspose.cells
from aspose.cells import Workbook, FileFormatType

workbook = Workbook(FileFormatType.XLSX)
workbook.worksheets.get(0).cells.get("A1").put_value("Hello World")
workbook.save("output.xlsx")
