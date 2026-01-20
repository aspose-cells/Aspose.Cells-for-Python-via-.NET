import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_get_chart_subtitle_for_ods_file():
    source_dir = get_source_directory()
    workbook = cells.Workbook(os.path.join(source_dir, "SampleChart.ods"))
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]
    print("Chart Subtitle: " + chart.sub_title.text)
    print("GetChartSubTitleForODSFile executed successfully.")

if __name__ == "__main__":
    run_get_chart_subtitle_for_ods_file()