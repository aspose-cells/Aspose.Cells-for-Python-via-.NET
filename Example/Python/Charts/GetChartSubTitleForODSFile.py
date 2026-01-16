import os
from aspose.cells import Workbook
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_get_chart_subtitle_for_ods_file():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "SampleChart.ods")

    workbook = Workbook(workbook_path)
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    print("Chart Subtitle: " + chart.sub_title.text)

    print("GetChartSubTitleForODSFile executed successfully.")

if __name__ == "__main__":
    run_get_chart_subtitle_for_ods_file()