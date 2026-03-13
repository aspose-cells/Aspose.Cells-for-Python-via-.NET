import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, LoadOptions
from aspose.cells import MemorySetting

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "KnowledgeBase" / "FAQs" / "FixOutOfMemoryException"

def run():
    data_dir = get_data_dir()
    options = LoadOptions()
    options.memory_setting = MemorySetting.MEMORY_PREFERENCE
    book = Workbook(str(data_dir / "sample.xlsx"), options)
    print("File has been loaded successfully")

if __name__ == "__main__":
    run()