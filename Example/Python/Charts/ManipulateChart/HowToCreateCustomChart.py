import os
import aspose.cells as cells
from aspose.cells.charts import ChartType

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_how_to_create_custom_chart():
    # Create a new workbook and get the first worksheet
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Populate cells with sample data
    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("A4").put_value(110)
    worksheet.cells.get("B1").put_value(260)
    worksheet.cells.get("B2").put_value(12)
    worksheet.cells.get("B3").put_value(50)
    worksheet.cells.get("B4").put_value(100)

    # Add a column chart to the worksheet
    chart_index = worksheet.charts.add(ChartType.COLUMN, 5, 0, 25, 10)

    # Access the newly added chart
    chart = worksheet.charts[chart_index]

    # Add NSeries data source ranging from A1 to B4
    chart.n_series.add("A1:B4", True)

    # Set the second NSeries to be a line chart
    chart.n_series[1].type = ChartType.LINE

    # Save the workbook
    output_path = os.path.join(get_output_directory(), "outputHowToCreateCustomChart.xlsx")
    workbook.save(output_path)

    print("HowToCreateCustomChart executed successfully.")

if __name__ == "__main__":
    run_how_to_create_custom_chart()