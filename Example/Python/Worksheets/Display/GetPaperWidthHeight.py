import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    from pathlib import Path
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    from pathlib import Path
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    from pathlib import Path
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "Display" / "GetPaperWidthHeight"

def run():
    # Create workbook
    wb = cells.Workbook()

    # Access first worksheet
    ws = wb.worksheets[0]

    # Set paper size to A2 and print paper width and height in inches
    ws.page_setup.paper_size = cells.PaperSizeType.PAPER_A2
    print(f"PaperA2: {ws.page_setup.paper_width}x{ws.page_setup.paper_height}")

    # Set paper size to A3 and print paper width and height in inches
    ws.page_setup.paper_size = cells.PaperSizeType.PAPER_A3
    print(f"PaperA3: {ws.page_setup.paper_width}x{ws.page_setup.paper_height}")

    # Set paper size to A4 and print paper width and height in inches
    ws.page_setup.paper_size = cells.PaperSizeType.PAPER_A4
    print(f"PaperA4: {ws.page_setup.paper_width}x{ws.page_setup.paper_height}")

    # Set paper size to Letter and print paper width and height in inches
    ws.page_setup.paper_size = cells.PaperSizeType.PAPER_LETTER
    print(f"PaperLetter: {ws.page_setup.paper_width}x{ws.page_setup.paper_height}")

if __name__ == "__main__":
    run()