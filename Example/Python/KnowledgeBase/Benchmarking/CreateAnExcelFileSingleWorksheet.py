import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "KnowledgeBase" / "Benchmarking" / "CreateAnExcelFileSingleWorksheet"

def create_aspose_cells_file(filename):
    start = datetime.now()
    workbook = cells.Workbook()
    ws = workbook.worksheets[0]
    for row in range(10000):
        for col in range(30):
            ws.cells.get(row, col).put_value(f"{row},{col}")
    workbook.save(filename)
    end = datetime.now()
    time_delta = end - start
    print("File Created! \n" + "Time consumed (Seconds): " + str(time_delta.total_seconds()))

def run():
    data_dir = get_data_dir()
    try:
        output_path = os.path.join(str(data_dir), "CellsSample_out.xls")
        create_aspose_cells_file(output_path)
    except Exception as ex:
        print("Error: " + str(ex))

if __name__ == "__main__":
    run()