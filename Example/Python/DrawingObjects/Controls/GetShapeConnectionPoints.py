import aspose.cells as cells

def run_get_shape_connection_points():
    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Get the first worksheet in the workbook.
    worksheet = workbook.worksheets[0]

    # Add a new textbox to the worksheet.
    textbox_index = worksheet.text_boxes.add(2, 1, 160, 200)

    # Access the textbox as a shape from the shapes collection.
    shape = workbook.worksheets[0].shapes[0]

    # Get all connection points of the shape.
    connection_points = shape.get_connection_points()

    # Display all the shape points.
    for pt in connection_points:
        print(f"X = {pt[0]}, Y = {pt[1]}")

    print("GetShapeConnectionPoints executed successfully.")

if __name__ == "__main__":
    run_get_shape_connection_points()