#import the python package
import aspose.cells
from aspose.cells import License,Workbook,FileFormatType
workbook = Workbook("bookwithChart.xlsx")
#save this workbook to resultFile,you can see a chart while open the file with MS-Excel*/
workbook.save("Convert.pdf");
