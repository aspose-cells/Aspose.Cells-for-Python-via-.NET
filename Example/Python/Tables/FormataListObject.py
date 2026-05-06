import os
from pathlib import Path
from aspose.cells import Workbook
from aspose.cells.tables import TableStyleType, TotalsCalculation

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/FormataListObject"

def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = Workbook()
    sheet = workbook.worksheets[0]
    cells = sheet.cells
    
    # Setting headers
    cells.get("A1").put_value("Employee")
    cells.get("B1").put_value("Quarter")
    cells.get("C1").put_value("Product")
    cells.get("D1").put_value("Continent")
    cells.get("E1").put_value("Country")
    cells.get("F1").put_value("Sale")
    
    # Setting data values
    cells.get("A2").put_value("David")
    cells.get("A3").put_value("David")
    cells.get("A4").put_value("David")
    cells.get("A5").put_value("David")
    cells.get("A6").put_value("James")
    cells.get("A7").put_value("James")
    cells.get("A8").put_value("James")
    cells.get("A9").put_value("James")
    cells.get("A10").put_value("James")
    cells.get("A11").put_value("Miya")
    cells.get("A12").put_value("Miya")
    cells.get("A13").put_value("Miya")
    cells.get("A14").put_value("Miya")
    cells.get("A15").put_value("Miya")
    
    cells.get("B2").put_value(1)
    cells.get("B3").put_value(2)
    cells.get("B4").put_value(3)
    cells.get("B5").put_value(4)
    cells.get("B6").put_value(1)
    cells.get("B7").put_value(2)
    cells.get("B8").put_value(3)
    cells.get("B9").put_value(4)
    cells.get("B10").put_value(4)
    cells.get("B11").put_value(1)
    cells.get("B12").put_value(1)
    cells.get("B13").put_value(2)
    cells.get("B14").put_value(2)
    cells.get("B15").put_value(2)
    
    cells.get("C2").put_value("Maxilaku")
    cells.get("C3").put_value("Maxilaku")
    cells.get("C4").put_value("Chai")
    cells.get("C5").put_value("Maxilaku")
    cells.get("C6").put_value("Chang")
    cells.get("C7").put_value("Chang")
    cells.get("C8").put_value("Chang")
    cells.get("C9").put_value("Chang")
    cells.get("C10").put_value("Chang")
    cells.get("C11").put_value("Geitost")
    cells.get("C12").put_value("Chai")
    cells.get("C13").put_value("Geitost")
    cells.get("C14").put_value("Geitost")
    cells.get("C15").put_value("Geitost")
    
    cells.get("D2").put_value("Asia")
    cells.get("D3").put_value("Asia")
    cells.get("D4").put_value("Asia")
    cells.get("D5").put_value("Asia")
    cells.get("D6").put_value("Europe")
    cells.get("D7").put_value("Europe")
    cells.get("D8").put_value("Europe")
    cells.get("D9").put_value("Europe")
    cells.get("D10").put_value("Europe")
    cells.get("D11").put_value("America")
    cells.get("D12").put_value("America")
    cells.get("D13").put_value("America")
    cells.get("D14").put_value("America")
    cells.get("D15").put_value("America")
    
    cells.get("E2").put_value("China")
    cells.get("E3").put_value("India")
    cells.get("E4").put_value("Korea")
    cells.get("E5").put_value("India")
    cells.get("E6").put_value("France")
    cells.get("E7").put_value("France")
    cells.get("E8").put_value("Germany")
    cells.get("E9").put_value("Italy")
    cells.get("E10").put_value("France")
    cells.get("E11").put_value("U.S.")
    cells.get("E12").put_value("U.S.")
    cells.get("E13").put_value("Brazil")
    cells.get("E14").put_value("U.S.")
    cells.get("E15").put_value("U.S.")
    
    cells.get("F2").put_value(2000)
    cells.get("F3").put_value(500)
    cells.get("F4").put_value(1200)
    cells.get("F5").put_value(1500)
    cells.get("F6").put_value(500)
    cells.get("F7").put_value(1500)
    cells.get("F8").put_value(800)
    cells.get("F9").put_value(900)
    cells.get("F10").put_value(500)
    cells.get("F11").put_value(1600)
    cells.get("F12").put_value(600)
    cells.get("F13").put_value(2000)
    cells.get("F14").put_value(500)
    cells.get("F15").put_value(900)
    
    # Add list object (table)
    list_object_index = sheet.list_objects.add(0, 0, 14, 5, True)
    list_object = sheet.list_objects[list_object_index]
    
    # Apply formatting
    list_object.table_style_type = TableStyleType.TABLE_STYLE_MEDIUM10
    list_object.show_totals = True
    list_object.list_columns[1].totals_calculation = TotalsCalculation.COUNT
    
    # Save file
    workbook.save(str(data_dir / "output.xlsx"))

if __name__ == "__main__":
    run()