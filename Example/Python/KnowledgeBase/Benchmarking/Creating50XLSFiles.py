import os
import datetime
import aspose.cells as cells

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "KnowledgeBase", "Benchmarking", "Creating50XLSFiles")

def run():
    data_dir = get_data_dir()
    
    try:
        create_aspose_cells_files(os.path.join(data_dir, "AsposeSample"))
    except Exception as ex:
        print(ex)

def create_aspose_cells_files(filename):
    start = datetime.datetime.now()
    for wkb in range(50):
        workbook = cells.Workbook()
        workbook.worksheets.remove_by_index(0)
        for i in range(5):
            ws = workbook.worksheets[workbook.worksheets.add()]
            ws.name = str(i)
            for row in range(150):
                for col in range(50):
                    ws.cells.get(row, col).put_value("row" + str(row) + " col" + str(col))
        workbook.save(filename + str(wkb) + "_out.xls")
    end = datetime.datetime.now()
    time = end - start
    print("50 File(s) Created! \n" + "Time consumed (Seconds): " + str(time.total_seconds()))

if __name__ == "__main__":
    run()