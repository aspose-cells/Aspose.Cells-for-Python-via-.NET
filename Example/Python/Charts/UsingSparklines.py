import os
import aspose.cells as cells
from aspose.cells.charts import SparklineType
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_using_sparklines():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the template workbook
    input_file = os.path.join(source_dir, "sampleUsingSparklines.xlsx")
    workbook = cells.Workbook(input_file)
    worksheet = workbook.worksheets[0]

    # Read existing sparklines (if any)
    for g in worksheet.sparkline_groups:
        print(f"sparkline group: type:{g.type}, sparkline items count:{len(g.sparklines)}")
        for s in g.sparklines:
            print(f"sparkline: row:{s.row}, col:{s.column}, dataRange:{s.data_range}")

    # Define the CellArea D2:D10
    ca = cells.CellArea()
    ca.start_column = 4
    ca.end_column = 4
    ca.start_row = 1
    ca.end_row = 7

    # Add new sparklines for a data range to the defined cell area
    idx = worksheet.sparkline_groups.add(
        SparklineType.COLUMN,
        "Sheet1!B2:D8",
        False,
        ca
    )
    group = worksheet.sparkline_groups[idx]

    # Create CellsColor and set series color
    clr = workbook.create_cells_color()
    clr.color = Color.orange
    group.series_color = clr

    # Save the workbook
    output_file = os.path.join(output_dir, "outputUsingSparklines.xlsx")
    workbook.save(output_file)

    print("UsingSparklines executed successfully.")

if __name__ == "__main__":
    run_using_sparklines()
