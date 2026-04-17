import os
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    workbook = Workbook(os.path.join(source_dir, "SampleSlicerChart.xlsx"))
    workbook.save(os.path.join(output_dir, "SampleSlicerChart.pdf"), SaveFormat.PDF)
    
    print("ExportSlicerToPDF executed successfully.")

if __name__ == "__main__":
    run()