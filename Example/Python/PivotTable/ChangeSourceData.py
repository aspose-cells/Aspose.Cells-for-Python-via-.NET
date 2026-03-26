import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "PivotTableExamples", "ChangeSourceData")

def Run():
    data_dir = get_data_dir()
    
    input_path = os.path.join(data_dir, "Book1.xlsx")
    
    workbook = cells.Workbook(input_path)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.get("A9").put_value("Golf")
    worksheet.cells.get("B9").put_value("Qtr4")
    worksheet.cells.get("C9").put_value(7000)
    
    range_obj = worksheet.cells.create_range(0, 0, 9, 3)
    range_obj.name = "DataSource"
    
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    Run()