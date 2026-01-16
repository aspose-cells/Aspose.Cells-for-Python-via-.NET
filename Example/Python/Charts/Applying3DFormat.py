import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_applying_3d_format():
    output_dir = get_output_directory()

    # Create a new workbook and set up worksheets
    book = Workbook()
    book.worksheets[0].name = "DataSheet"
    data_sheet = book.worksheets.get("DataSheet")
    sheet = book.worksheets.add("MyChart")

    # Fill data sheet with values
    data_sheet.cells.get("B1").put_value(1)
    data_sheet.cells.get("B2").put_value(2)
    data_sheet.cells.get("B3").put_value(3)
    data_sheet.cells.get("A1").put_value("A")
    data_sheet.cells.get("A2").put_value("B")
    data_sheet.cells.get("A3").put_value("C")

    # Add a column chart
    charts = sheet.charts
    charts.add(ChartType.COLUMN, 5, 0, 25, 15)

    chart = book.worksheets.get("MyChart").charts[0]

    # Set background/foreground colors
    chart.plot_area.area.background_color = Color.white
    chart.chart_area.area.background_color = Color.white
    chart.plot_area.area.foreground_color = Color.white
    chart.chart_area.area.foreground_color = Color.white

    # Hide legend and set data
    chart.show_legend = False
    chart.n_series.add("DataSheet!B1:B3", True)
    chart.n_series.category_data = "DataSheet!A1:A3"

    # Access the first series
    ser = chart.n_series[0]

    # Apply 3‑D formatting
    sp_pr = ser.shape_properties
    fmt3d = sp_pr.format_3d

    bevel = fmt3d.top_bevel
    bevel.type = BevelPresetType.CIRCLE
    bevel.height = 2.0
    bevel.width = 5.0

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