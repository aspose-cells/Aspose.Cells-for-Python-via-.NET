import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "KnowledgeBase/ComparingVSTOWithAspose/VSTOCode")

def run():
    try:
        data_dir = get_data_dir()
        
        start = datetime.now()
        workbook = cells.Workbook(os.path.join(data_dir, "TempBook.xls"))
        
        worksheet = workbook.worksheets[0]
        cs = worksheet.cells
        
        for i in range(1, 1001):
            for j in range(1, 21):
                cs.get(i, j).put_value(f"Row {i} Col {j}")
        
        output_path = os.path.join(data_dir, "TempBook1_out.xls")
        workbook.save(output_path)
        
        end = datetime.now()
        time = end - start
        print(f"File Created! Time consumed (Seconds): {time.total_seconds()}")
        
    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    run()