import os
from datetime import datetime
from aspose.cells import Workbook

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "KnowledgeBase", "Benchmarking", "CreateAnExcelFileFiveSheets")

def create_aspose_cells_file(filename):
    start = datetime.now()
    workbook = Workbook()
    workbook.worksheets.remove_by_index(0)
    for i in range(5):
        worksheet = workbook.worksheets[workbook.worksheets.add()]
        worksheet.name = str(i)
        for row in range(150):
            for col in range(56):
                worksheet.cells.get(row, col).put_value(f"row{row} col{col}")
    workbook.save(filename)
    end = datetime.now()
    time_diff = end - start
    print("File Created! \n" + "Time consumed (Seconds): " + str(time_diff.total_seconds()))

def run():
    data_dir = get_data_dir()
    try:
        create_aspose_cells_file(os.path.join(data_dir, "ACellsSample_out.xls"))
    except Exception as ex:
        print("Error: " + str(ex))

if __name__ == "__main__":
    run()