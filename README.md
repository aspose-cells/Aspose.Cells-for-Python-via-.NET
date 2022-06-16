# Spreadsheet Processing Python High Code API

[Product Page](https://products.aspose.com/cells/python-net) | [Docs](https://docs.aspose.com/cells/python-net/) | [Demos](https://products.aspose.app/cells/family/) | [API Reference](https://reference.aspose.com/cells/net/) | [Examples](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) | [Blog](https://blog.aspose.com/category/cells/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license)

[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) is a scalable and feature-rich API to process Excel&reg; spreadsheets using Python. API offers Excel&reg; file creation, manipulation, conversion and rendering. Developers can format worksheets, rows, columns or cells to the most granular level, create manipulate chart and pivot tables, render worksheets, charts and specific data ranges to PDF or images, add calculate Excel&reg;'s built-in and custom formulas and much more - all without any dependency on Microsoft Office or Excel&reg; application.

## Spreadsheet Python via .NET On-premise API Features

- Spreadsheet generation & manipulation via API.
- High-quality file format conversion & rendering.
- Print Microsoft Excel&reg; files to physical or virtual printers.
- Combine, modify, protect, or parse Excel&reg; sheets.
- Apply worksheet formatting.
- Configure and apply page setup for the worksheets.
- Create & customize Excel&reg; charts, Pivot Tables, conditional
  formatting rules, slicers, tables & spark-lines.
- Convert Excel&reg; charts to images & PDF.
- Convert Excel&reg; files to various other formats.
- Formula calculation engine that supports all basic and advanced Excel&reg; functions.

Please visit the [official documentation](https://docs.aspose.com/cells/python-net/) for a more detailed list of features.

## Read & Write Sreadsheet File Formats

**Microsoft Excel&reg;:** XLS, XLSX, XLSB, XLSM, XLT, XLTX, XLTM, CSV, TSV, TabDelimited, SpreadsheetML\
**OpenOffice:** ODS, SXC, FODS\
**Text:** TXT\
**Web:** HTML, MHTML\
**iWork&reg;:** Numbers\
**Other:** SXC, FODS

## Save Spreadsheet Files AS

**Microsoft Word&reg;:** DOCX\
**Microsoft PowerPoint&reg;:** PPTX\
**Microsoft Excel&reg;:** XLAM\
**Fixed Layout:** PDF, XPS\
**Data Interchange:** DIF\
**Vector Graphics:** SVG\
**Image:** TIFF,PNG, BMP, JPEG, GIF\
**Meta File:** EMF\
**Markdown:** MD

Please visit [Supported File Formats](https://docs.aspose.com/cells/python-net/supported-file-formats/) for further details.

## System Requirements

Your machine does not need to have Microsoft Excel&reg; or OpenOffice&reg; software installed.

### Supported Operating Systems

**Microsoft Windows&reg;:** Windows Desktop & Server (`x64`, `x86`)\
**Linux:** Ubuntu, OpenSUSE, CentOS, and others\
**Other:** Any operating system (OS) that can install Mono(.NET 4.0 Framework support) or use .NET core.

## Get Started

### Installation via `pip`

The Aspose.Cells for Python via .NET is [available at pypi.org](https://pypi.org/project/aspose-cells-python/). To install it, please run the following command:

`pip install aspose-cells-python`

### Create Excel&reg; File from scratch using Python

```python
#import the python package
import aspose.cells
from aspose.cells import License,Workbook,FileFormatType

#Create a new Workbook
workbook = Workbook()

#Get the first worksheet
worksheet=workbook.worksheets[0]

#Get the "A1" cell
cells=worksheet.cells
cell=cells.get("A1")

#Write "Hello World" to  "A1" in the first sheet
cell.put_value("Hello World!")

#save this workbook to XLSX 
workbook.save("HelloWorld.xlsx")
```

## Convert Excel&reg; `XLSX` File to `PDF` using Python

```python
#import the python package
import aspose.cells
from aspose.cells import License,Workbook,FileFormatType

#Open a existing Workbook
workbook = Workbook("bookwithChart.xlsx")

#save this workbook to PDF file,you can see a chart while open the file with MS Excel&reg;*/
workbook.save("Convert.pdf");
```

## Create Excel File and set style for the cells

```python
#import the python package
import aspose.cells as ac
import aspose.pydrawing as ad
from aspose.cells import Workbook,FileFormatType

#Create a new Workbook
workbook = Workbook()
worksheet=workbook.worksheets[0]

#get cell style
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

#save this workbook 
workbook.save("Style.xlsx")
```

[Product Page](https://products.aspose.com/cells/python-net) | [Docs](https://docs.aspose.com/cells/python-net/) | [Demos](https://products.aspose.app/cells/family/) | [API Reference](https://reference.aspose.com/cells/net/) | [Examples](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) | [Blog](https://blog.aspose.com/category/cells/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license)
