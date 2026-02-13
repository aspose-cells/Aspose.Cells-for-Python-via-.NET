import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "Files" / "Handling" / "LoadVisibleSheetsOnly"
    ).resolve()

def run():
    # ExStart:1
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    sample_path = data_dir / "output.xlsx"

    # Create a sample workbook and put data in the first cell of three sheets
    create_wb = cells.Workbook()
    create_wb.worksheets.get("Sheet1").cells.get("A1").put_value("Aspose")
    create_wb.worksheets.add("Sheet2").cells.get("A1").put_value("Aspose")
    create_wb.worksheets.add("Sheet3").cells.get("A1").put_value("Aspose")
    create_wb.worksheets.get("Sheet3").is_visible = False
    create_wb.save(str(sample_path))

    # Load the workbook (custom LoadFilter not supported in Python API)
    load_wb = cells.Workbook(str(sample_path))

    # Emulate loading only visible sheets: clear data from hidden worksheets
    for ws in load_wb.worksheets:
        if not ws.is_visible:
            ws.cells.clear()  # keep structure, remove cell data

    print(f"Sheet1: A1: {load_wb.worksheets.get('Sheet1').cells.get('A1').value}")
    print(f"Sheet2: A1: {load_wb.worksheets.get('Sheet2').cells.get('A1').value}")
    print(f"Sheet3: A1: {load_wb.worksheets.get('Sheet3').cells.get('A1').value}")
    # ExEnd:1

if __name__ == "__main__":
    run()
