import os
import datetime
import aspose.cells as cells


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "KnowledgeBase", "Benchmarking", "LoadLargeExcelScenario2")


def run():
    data_dir = get_data_dir()
    
    try:
        create_aspose_cells_file(
            os.path.join(data_dir, "Sample.xls"),
            os.path.join(data_dir, "output_out.xls")
        )
    except Exception as ex:
        print(str(ex))


def create_aspose_cells_file(filename_in, filename_out):
    start = datetime.datetime.now()
    workbook = cells.Workbook(filename_in)
    
    for i in range(100):
        ws = workbook.worksheets[i]
        cells_obj = ws.cells
        cells_obj.insert_rows(0, 100)
        for r in range(100):
            cells_obj.get(r, 0).put_value("This is testing row #: " + str(r))
    
    workbook.save(filename_out)
    end = datetime.datetime.now()
    time_diff = end - start
    print("File Updated! \n" + "Time consumed (Seconds): " + str(time_diff.total_seconds()))


if __name__ == "__main__":
    run()