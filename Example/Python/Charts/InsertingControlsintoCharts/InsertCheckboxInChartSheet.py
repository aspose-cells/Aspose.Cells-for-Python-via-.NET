import os
import aspose.cells as cells
from aspose.cells.charts import ChartType
from aspose.cells.drawing import MsoDrawingType, PlacementType
from aspose.cells import SheetType


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_insert_checkbox_in_chart_sheet():
    workbook = cells.Workbook()
    index = workbook.worksheets.add(SheetType.CHART)

    sheet = workbook.worksheets[index]
    sheet.charts.add_floating_chart(ChartType.COLUMN, 0, 0, 1024, 960)
    sheet.charts[0].n_series.add("{1,2,3}", False)

    sheet.charts[0].shapes.add_shape_in_chart(
        MsoDrawingType.CHECK_BOX, PlacementType.MOVE, 400, 400, 1000, 600
    )
    sheet.charts[0].shapes[0].text = "CheckBox 1"

    output_path = os.path.join(get_output_directory(), "InsertCheckboxInChartSheet_out.xlsx")
    workbook.save(output_path)


if __name__ == "__main__":
    run_insert_checkbox_in_chart_sheet()