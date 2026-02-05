import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (Path(__file__).parent / ".." / ".." / "Data" /
            "DrawingObjects" / "Pictures" / "PictureCellReference")

def run_picture_cell_reference():
    try:
        # Instantiate a new Workbook
        workbook = cells.Workbook()
        # Get the first worksheet's cells collection
        sheet_cells = workbook.worksheets[0].cells

        # Add string values to the cells
        sheet_cells.get("A1").put_value("A1")
        sheet_cells.get("C10").put_value("C10")

        # Add a blank picture to the D1 cell
        picture = workbook.worksheets[0].shapes.add_picture(0, 3, 10, 6, None)

        # Specify the formula that refers to the source range of cells
        picture.formula = "A1:C10"

        # Update the shapes selected value in the worksheet
        workbook.worksheets[0].shapes.update_selected_value()

        # Save the Excel file
        output_file = os.path.join(get_data_dir(), "output.out.xls")
        workbook.save(output_file)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    run_picture_cell_reference()