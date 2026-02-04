import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir() -> Path:
    # Adjust the relative path if the Excel file is stored elsewhere
    return (Path(__file__).parent / ".." / ".." / "Data").resolve()

def run_access_non_primitive_shape() -> None:
    data_dir = get_data_dir()
    workbook_path = data_dir / "NonPrimitiveShape.xlsx"

    if not workbook_path.is_file():
        print(f"File not found: {workbook_path}")
        return

    workbook = cells.Workbook(str(workbook_path))
    worksheet = workbook.worksheets[0]

    # Access the user‑defined shape
    shape = worksheet.shapes[0]

    if shape.auto_shape_type == cells.drawing.AutoShapeType.NOT_PRIMITIVE:
        # Access shape's data
        shape_path_collection = shape.paths

        for shape_path in shape_path_collection:
            # Access path segment list
            path_segments = shape_path.path_segement_list

            for path_segment in path_segments:
                # Get the points in the path segment
                segment_points = path_segment.points

                for path_point in segment_points:
                    print(f"X: {path_point.x}, Y: {path_point.y}")

if __name__ == "__main__":
    run_access_non_primitive_shape()
