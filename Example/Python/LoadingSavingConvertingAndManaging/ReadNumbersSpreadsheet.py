import os
from pathlib import Path
from aspose.cells import Workbook, LoadOptions, SaveFormat, LoadFormat

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    opts = LoadOptions(LoadFormat.NUMBERS)
    wb = Workbook(str(source_dir / "sampleNumbersByAppleInc.numbers"), opts)
    wb.save(str(output_dir / "outputNumbersByAppleInc.pdf"), SaveFormat.PDF)

if __name__ == "__main__":
    run()