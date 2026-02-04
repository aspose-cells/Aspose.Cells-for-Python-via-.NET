import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run_send_shape_front_or_back_in_worksheet():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load source Excel file
    input_path = os.path.join(source_dir, "sampleToFrontOrBack.xlsx")
    wb = cells.Workbook(input_path)

    # Access first worksheet
    ws = wb.worksheets[0]

    # Access first and fourth shape (indices are zero‑based)
    sh1 = ws.shapes[0]
    sh4 = ws.shapes[3]

    # Print the Z‑Order position of the shapes
    print(f"Z-Order Shape 1: {sh1.z_order_position}")

    # Send this shape to front (2 = move forward)
    sh1.to_front_or_back(2)

    print(f"Z-Order Shape 4: {sh4.z_order_position}")

    # Send this shape to back (-2 = move backward)
    sh4.to_front_or_back(-2)

    # Save the output Excel file
    output_path = os.path.join(output_dir, "outputToFrontOrBack.xlsx")
    wb.save(output_path)

    print("SendShapeFrontOrBackInWorksheet executed successfully.\n")

if __name__ == "__main__":
    run_send_shape_front_or_back_in_worksheet()