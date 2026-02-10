import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory").resolve()

def get_output_directory():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory").resolve()

def get_data_dir():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Utility" / "XlstoPDFDirectConversation").resolve()

def run():
    # Ensure source and output directories exist
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    data_dir = get_data_dir()
    # Load the workbook from the data directory
    workbook_path = data_dir / "Book1.xls"
    workbook = cells.Workbook(str(workbook_path))

    # Save the PDF to the output directory
    pdf_path = output_dir / "output.pdf"
    workbook.save(str(pdf_path), cells.SaveFormat.PDF)

if __name__ == "__main__":
    run()