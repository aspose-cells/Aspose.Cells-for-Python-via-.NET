import os
from aspose import pydrawing as drawing
import aspose.cells as cells
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "KnowledgeBase/FAQs/FileFormatInformation"

def run():
    data_dir = get_data_dir()
    
    # Load File
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "sample.xls"))
    print(finfo.file_format_type)
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "Encrypted.xlsx"))
    print(finfo.file_format_type)
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "Test data.docx"))
    print(finfo.file_format_type)
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "Test data encrypted.docx"))
    print(finfo.file_format_type)
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "Test data.pptx"))
    print(finfo.file_format_type)
    finfo = cells.FileFormatUtil.detect_file_format(str(data_dir / "Test data encrypted.pptx"))
    print(finfo.file_format_type)

if __name__ == "__main__":
    run()