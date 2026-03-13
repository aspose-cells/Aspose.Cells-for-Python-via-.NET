import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "KnowledgeBase", "Benchmarking", "LoadLargeExcelScenario3")

def run():
    data_dir = get_data_dir()
    
    try:
        create_aspose_cells_file(os.path.join(data_dir, "Sample.xls"), os.path.join(data_dir, "output_out.xls"))
    except Exception as ex:
        print(ex)

def create_aspose_cells_file(filename_in, filename_out):
    start = datetime.now()
    workbook = Workbook(filename_in)
    for i in range(100):
        ws = workbook.worksheets[i]
        cells = ws.cells
        for c in range(10):
            cells.insert_column(c)
            cells.get(0, c).put_value("Column" + str(c))
    workbook.save(filename_out)
    end = datetime.now()
    time_delta = end - start
    print("File Updated! \n" + "Time consumed (Seconds): " + str(time_delta.total_seconds()))

if __name__ == "__main__":
    run()