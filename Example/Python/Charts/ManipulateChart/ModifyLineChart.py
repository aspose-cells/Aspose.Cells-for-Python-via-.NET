import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_modify_line_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "sampleModifyLineChart.xlsx")
    workbook = cells.Workbook(input_path)

    chart = workbook.worksheets[0].charts[0]

    chart.n_series.add("{60, 80, 10}", True)
    chart.n_series.add("{0.3, 0.7, 1.2}", True)

    chart.n_series[3].plot_on_second_axis = True

    chart.n_series[1].border.color = Color.green
    chart.n_series[2].border.color = Color.red

    chart.second_value_axis.is_visible = True

    output_path = os.path.join(output_dir, "outputModifyLineChart.xlsx")
    workbook.save(output_path)

    print("ModifyLineChart executed successfully.")

if __name__ == "__main__":
    run_modify_line_chart()