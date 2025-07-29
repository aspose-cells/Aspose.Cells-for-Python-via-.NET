# import the python package
import aspose.cells
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("HelloWorld.xlsx")
# Saving this workbook to PDF
workbook.save("HelloWorld.pdf")