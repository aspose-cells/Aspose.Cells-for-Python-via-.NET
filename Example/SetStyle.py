import aspose.cells as ac
import aspose.pydrawing as ad
from aspose.cells import License,Workbook,FileFormatType
workbook = Workbook()
worksheet=workbook.worksheets[0]
#get cells style
style=worksheet.cells.style
#set font color
style.font.color=ad.Color.green
#set pattern
style.pattern=ac.BackgroundType.GRAY12
#set Background
style.background_color = ad.Color.red
#set Border
style.set_border(ac.BorderType.LEFT_BORDER,ac.CellBorderType.THIN,ad.Color.blue)
style.set_border(ac.BorderType.RIGHT_BORDER,ac.CellBorderType.DOUBLE,ad.Color.gold)
#set string value to cell 'A1'
cells=worksheet.cells
cell=cells.get("A1")
cell.put_value("Text")
#apply style to cell 'A1'
cell.set_style(style)
#save this workbook to resultFile
workbook.save("Style.xlsx")
