import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_find_type_of_x_and_y_values_of_points_in_chart_series():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx")
    wb = cells.Workbook(workbook_path)
    ws = wb.worksheets[0]
    ch = ws.charts[0]
    ch.calculate()
    pnt = ch.n_series[0].points[0]
    print("X Value Type: " + str(pnt.x_value_type))
    print("Y Value Type: " + str(pnt.y_value_type))
    print("FindTypeOfXandYValuesOfPointsInChartSeries executed successfully.")

if __name__ == "__main__":
    run_find_type_of_x_and_y_values_of_points_in_chart_series()