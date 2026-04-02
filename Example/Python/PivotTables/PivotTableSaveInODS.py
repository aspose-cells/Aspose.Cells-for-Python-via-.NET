import os
from pathlib import Path
import aspose.cells as cells
from aspose.cells.pivot import PivotFieldType

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    output_dir = get_output_directory()
    
    os.makedirs(output_dir, exist_ok=True)
    
    workbook = cells.Workbook()
    
    worksheet = workbook.worksheets[0]
    
    cells_obj = worksheet.cells
    
    cells_obj.get("A1").put_value("Sport")
    cells_obj.get("B1").put_value("Quarter")
    cells_obj.get("C1").put_value("Sales")
    
    cells_obj.get("A2").put_value("Golf")
    cells_obj.get("A3").put_value("Golf")
    cells_obj.get("A4").put_value("Tennis")
    cells_obj.get("A5").put_value("Tennis")
    cells_obj.get("A6").put_value("Tennis")
    cells_obj.get("A7").put_value("Tennis")
    cells_obj.get("A8").put_value("Golf")
    
    cells_obj.get("B2").put_value("Qtr3")
    cells_obj.get("B3").put_value("Qtr4")
    cells_obj.get("B4").put_value("Qtr3")
    cells_obj.get("B5").put_value("Qtr4")
    cells_obj.get("B6").put_value("Qtr3")
    cells_obj.get("B7").put_value("Qtr4")
    cells_obj.get("B8").put_value("Qtr3")
    
    cells_obj.get("C2").put_value(1500)
    cells_obj.get("C3").put_value(2000)
    cells_obj.get("C4").put_value(600)
    cells_obj.get("C5").put_value(1500)
    cells_obj.get("C6").put_value(4070)
    cells_obj.get("C7").put_value(5000)
    cells_obj.get("C8").put_value(6430)
    
    pivot_tables = worksheet.pivot_tables
    
    index = pivot_tables.add("=A1:C8", "E3", "PivotTable2")
    
    pivot_table = pivot_tables[index]
    
    pivot_table.row_grand = False
    
    pivot_table.add_field_to_area(PivotFieldType.UNDEFINED, 0)
    pivot_table.add_field_to_area(PivotFieldType.ROW, 1)
    pivot_table.add_field_to_area(PivotFieldType.COLUMN, 2)
    
    pivot_table.calculate_data()
    
    output_path = os.path.join(output_dir, "PivotTableSaveInODS_out.ods")
    workbook.save(output_path)
    
    print("PivotTableSaveInODS executed successfully.")

if __name__ == "__main__":
    main()