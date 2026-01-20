import os
import aspose.cells as cells
from aspose.cells import Workbook
from aspose.cells.charts import ChartType
from aspose.cells.drawing import BevelPresetType, PresetMaterialType, LightRigType
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_applying_3d_format():
    output_dir = get_output_directory()

    # Instantiate a new Workbook
    book = cells.Workbook()

    # Rename the first worksheet
    book.worksheets[0].name = "DataSheet"

    # Add a Data Worksheet reference
    data_sheet = book.worksheets.get("DataSheet")

    # Add Chart Worksheet
    sheet = book.worksheets.add("MyChart")

    # Populate data worksheet
    data_sheet.cells.get("B1").put_value(1.0)
    data_sheet.cells.get("B2").put_value(2.0)
    data_sheet.cells.get("B3").put_value(3.0)
    data_sheet.cells.get("A1").put_value("A")
    data_sheet.cells.get("A2").put_value("B")
    data_sheet.cells.get("A3").put_value("C")

    # Add a Column chart
    sheet.charts.add(ChartType.COLUMN, 5, 0, 25, 15)

    # Get the newly added chart
    chart = sheet.charts[0]

    # Set background/foreground colors
    chart.plot_area.area.background_color = Color.white
    chart.chart_area.area.background_color = Color.white
    chart.plot_area.area.foreground_color = Color.white
    chart.chart_area.area.foreground_color = Color.white

    # Hide legend
    chart.show_legend = False

    # Add data series
    chart.n_series.add("DataSheet!B1:B3", True)
    chart.n_series.category_data = "DataSheet!A1:A3"

    # Get the series
    ser = chart.n_series[0]

    # Apply 3‑D formatting
    shape_props = ser.shape_properties
    fmt3d = shape_props.format_3d

    # Bevel settings
    bevel = fmt3d.top_bevel
    bevel.type = BevelPresetType.CIRCLE
    bevel.height = 2.0
    bevel.width = 5.0

    # Surface material and lighting
    fmt3d.surface_material_type = PresetMaterialType.WARM_MATTE
    fmt3d.surface_lighting_type = LightRigType.THREE_POINT
    fmt3d.lighting_angle = 20.0

    # Series colors
    ser.area.background_color = Color.maroon
    ser.area.foreground_color = Color.maroon
    ser.border.color = Color.maroon

    # Save the workbook
    output_path = os.path.join(output_dir, "outputApplying3DFormat.xlsx")
    book.save(output_path)

    print("Applying3DFormat executed successfully.")


if __name__ == "__main__":
    run_applying_3d_format()
