import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_how_to_create_line_chart():
    output_dir = get_output_directory()

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("B1").put_value(4)
    worksheet.cells.get("B2").put_value(20)
    worksheet.cells.get("B3").put_value(50)

    chart_index = worksheet.charts.add(cells.charts.ChartType.LINE, 5, 0, 25, 10)
    chart = worksheet.charts[chart_index]

    chart.n_series.add("A1:B3", True)

    output_path = os.path.join(output_dir, "outputHowToCreateLineChart.xlsx")
    workbook.save(output_path)

    print("HowToCreateLineChart executed successfully.")

if __name__ == "__main__":
    run_how_to_create_line_chart()