import os
from pathlib import Path
from aspose.cells import Workbook, SaveFormat
from datetime import datetime

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def convert_excel_file_to_markdown():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Open the template file
    workbook = Workbook(str(source_dir / "Book1.xlsx"))

    # Save as Markdown
    workbook.save(str(output_dir / "Book1.md"), SaveFormat.MARKDOWN)

    print("ConvertExcelFileToMarkdown executed successfully.")

if __name__ == "__main__":
    convert_excel_file_to_markdown()