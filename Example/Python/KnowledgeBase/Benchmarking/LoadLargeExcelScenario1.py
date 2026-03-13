import os
from datetime import datetime
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "KnowledgeBase" / "Benchmarking" / "LoadLargeExcelScenario1"

def run():
    data_dir = get_data_dir()
    
    try:
        create_aspose_cells_file(str(data_dir / "Sample.xls"), str(data_dir / "output_out.xls"))
    except Exception as ex:
        print(str(ex))

def create_aspose_cells_file(filename_in, filename_out):
    start = datetime.now()
    workbook = cells.Workbook(filename_in)
    for i in range(100):
        ws = workbook.worksheets[i]
        ws.cells.get(0, 0).put_value("Data" + str(i))
    workbook.save(filename_out)
    end = datetime.now()
    time_delta = end - start
    print("File Updated! \n" + "Time consumed (Seconds): " + str(time_delta.total_seconds()))

if __name__ == "__main__":
    run()