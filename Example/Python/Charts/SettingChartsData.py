import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_output_directory():
    return os.path.abspath(os.path.join(".",   "..", "..", "Data", "02_OutputDirectory"))

def run_setting_charts_data():
    output_dir = get_output_directory()

    workbook = Workbook()
    worksheet = workbook.worksheets[0]

    worksheet.cells.get("A1").put_value(50.0)
    worksheet.cells.get("A2").put_value(100.0)
    worksheet.cells.get("A3").put_value(170.0)
    worksheet.cells.get("A4").put_value(300.0)
    worksheet.cells.get("B1").put_value(160.0)
    worksheet.cells.get("B2").put_value(32.0)
    worksheet.cells.get("B3").put_value(50.0)
    worksheet.cells.get("B4").put_value(40.0)

    worksheet.cells.get("C1").put_value("Q1")
    worksheet.cells.get("C2").put_value("Q2")
    worksheet.cells.get("C3").put_value("Y1")
    worksheet.cells.get("C4").put_value("Y2")

    chart_index = worksheet.charts.add(ChartType.COLUMN, 5, 0, 15, 5)
    chart = worksheet.charts[chart_index]
    chart.n_series.add("A1:B4", True)

    output_file = os.path.join(output_dir, "outputSettingChartsData.xlsx")
    workbook.save(output_file)

    print("SettingChartsData executed successfully.")

if __name__ == "__main__":
    run_setting_charts_data()