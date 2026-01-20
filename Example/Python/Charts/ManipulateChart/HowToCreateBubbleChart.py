import os
import aspose.cells as cells
from aspose.cells.charts import ChartType

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_how_to_create_bubble_chart():
    output_dir = get_output_directory()

    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Obtaining the reference of the first worksheet by passing its index
    worksheet = workbook.worksheets[0]

    # Fill in data for chart's series
    worksheet.cells.get(0, 0).put_value("Y Values")
    worksheet.cells.get(0, 1).put_value(2)
    worksheet.cells.get(0, 2).put_value(4)
    worksheet.cells.get(0, 3).put_value(6)

    worksheet.cells.get(1, 0).put_value("Bubble Size")
    worksheet.cells.get(1, 1).put_value(2)
    worksheet.cells.get(1, 2).put_value(3)
    worksheet.cells.get(1, 3).put_value(1)

    worksheet.cells.get(2, 0).put_value("X Values")
    worksheet.cells.get(2, 1).put_value(1)
    worksheet.cells.get(2, 2).put_value(2)
    worksheet.cells.get(2, 3).put_value(3)

    # Adding a chart to the worksheet
    chart_index = worksheet.charts.add(ChartType.BUBBLE, 5, 0, 25, 10)

    # Accessing the instance of the newly added chart
    chart = worksheet.charts[chart_index]

    # Adding SeriesCollection (chart data source) to the chart ranging
    chart.n_series.add("B1:D1", True)

    # Set bubble sizes
    chart.n_series[0].bubble_sizes = "B2:D2"

    # Set X axis values
    chart.n_series[0].x_values = "B3:D3"

    # Set Y axis values
    chart.n_series[0].values = "B1:D1"

    # Saving the Excel file
    output_path = os.path.join(output_dir, "outputHowToCreateBubbleChart.xlsx")
    workbook.save(output_path)

    print("HowToCreateBubbleChart executed successfully.")

if __name__ == "__main__":
    run_how_to_create_bubble_chart()