import os
import aspose.cells as cells
from aspose.cells.charts import ChartType
from aspose.cells.drawing import MsoDrawingType, PlacementType

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_insert_checkbox_in_chart_sheet():
    output_dir = get_output_directory()
    workbook = cells.Workbook()
    index = workbook.worksheets.add(cells.SheetType.CHART)
    sheet = workbook.worksheets[index]

    sheet.charts.add_floating_chart(ChartType.COLUMN, 0, 0, 1024, 960)
    chart = sheet.charts[0]
    chart.n_series.add("{1,2,3}", False)

    chart.shapes.add_shape_in_chart(MsoDrawingType.CHECK_BOX, PlacementType.MOVE, 400, 400, 1000, 600)
    chart.shapes[0].text = "CheckBox 1"

    workbook.save(os.path.join(output_dir, "InsertCheckboxInChartSheet_out.xlsx"))

if __name__ == "__main__":
    run_insert_checkbox_in_chart_sheet()