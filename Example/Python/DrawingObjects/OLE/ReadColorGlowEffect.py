import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "OLE" / "ReadColorGlowEffect"

def run_read_color_glow_effect():
    data_dir = get_data_dir()
    input_file = os.path.join(data_dir, "sourceGlowEffectColor.xlsx")
    wb = cells.Workbook(input_file)
    ws = wb.worksheets[0]
    sh = ws.shapes[0]
    ge = sh.glow
    clr = ge.color
    print(f"Color: {clr.color}")
    print(f"ColorIndex: {clr.color_index}")
    print(f"IsShapeColor: {clr.is_shape_color}")
    print(f"Transparency: {clr.transparency}")
    print(f"Type: {clr.type}")

if __name__ == "__main__":
    run_read_color_glow_effect()
