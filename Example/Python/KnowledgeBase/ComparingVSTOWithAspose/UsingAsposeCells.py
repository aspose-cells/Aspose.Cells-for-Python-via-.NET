import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "KnowledgeBase/ComparingVSTOWithAspose/UsingAsposeCells"

def run():
    data_dir = get_data_dir()
    start = datetime.now()
    my_path = str(data_dir / "TempBook.xls")
    workbook = Workbook(my_path)
    ws = workbook.worksheets[0]

    for i in range(1000):
        for j in range(20):
            ws.cells.get(i, j).put_value(f"Row {i + 1} Col {j + 1}")

    output_path = str(data_dir / "TempBook1_out.xls")
    workbook.save(output_path)
    end = datetime.now()
    time = end - start
    print(f"File Created! Time consumed (Seconds): {time.total_seconds()}")