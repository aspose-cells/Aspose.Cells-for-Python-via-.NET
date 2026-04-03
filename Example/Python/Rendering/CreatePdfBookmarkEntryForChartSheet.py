import os
from pathlib import Path
from datetime import datetime
from aspose import cells
from aspose.pydrawing import Color
from aspose.cells import PdfSaveOptions
from aspose.cells.rendering import PdfBookmarkEntry

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Rendering/CreatePdfBookmarkEntryForChartSheet"

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    data_dir = get_data_dir()
    
    # Load sample Excel file
    wb = cells.Workbook(str(source_dir / "sampleCreatePdfBookmarkEntryForChartSheet.xlsx"))
    
    # Access all four worksheets
    sheet1 = wb.worksheets[0]
    sheet2 = wb.worksheets[1]
    sheet3 = wb.worksheets[2]
    sheet4 = wb.worksheets[3]
    
    # Create Pdf Bookmark Entry for Sheet1
    ent1 = PdfBookmarkEntry()
    ent1.destination = sheet1.cells.get("A1")
    ent1.text = "Bookmark-I"
    
    # Create Pdf Bookmark Entry for Sheet2 - Chart
    ent2 = PdfBookmarkEntry()
    ent2.destination = sheet2.cells.get("A1")
    ent2.text = "Bookmark-II-Chart1"
    
    # Create Pdf Bookmark Entry for Sheet3
    ent3 = PdfBookmarkEntry()
    ent3.destination = sheet3.cells.get("A1")
    ent3.text = "Bookmark-III"
    
    # Create Pdf Bookmark Entry for Sheet4 - Chart
    ent4 = PdfBookmarkEntry()
    ent4.destination = sheet4.cells.get("A1")
    ent4.text = "Bookmark-IV-Chart2"
    
    # Arrange all Bookmark Entries
    lst = []
    ent1.sub_entry = lst
    lst.append(ent2)
    lst.append(ent3)
    lst.append(ent4)
    
    # Create Pdf Save Options with Bookmark Entries
    opts = PdfSaveOptions()
    opts.bookmark = ent1
    
    # Save the output Pdf
    wb.save(str(output_dir / "outputCreatePdfBookmarkEntryForChartSheet.pdf"), opts)

if __name__ == "__main__":
    main()