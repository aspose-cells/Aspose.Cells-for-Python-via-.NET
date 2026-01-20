import os
import aspose.cells as cells
from aspose.cells.drawing import FillType
from aspose.cells import ThemeColor, ThemeColorType

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_applying_themes_in_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the workbook containing a chart
    workbook_path = os.path.join(source_dir, "sampleApplyingThemesInChart.xlsx")
    workbook = cells.Workbook(workbook_path)

    # Access the first worksheet
    worksheet = workbook.worksheets[0]

    # Access the first chart in the worksheet
    chart = worksheet.charts[0]

    # Set the fill type of the first series to solid
    chart.n_series[0].area.fill_format.fill_type = FillType.SOLID

    # Get the current CellsColor of the solid fill
    cc = chart.n_series[0].area.fill_format.solid_fill.cells_color

    # Apply an Accent6 theme color with 60% brightness
    cc.theme_color = ThemeColor(ThemeColorType.ACCENT6, 0.6)

    # Assign the modified CellsColor back to the series
    chart.n_series[0].area.fill_format.solid_fill.cells_color = cc

    # Save the modified workbook
    output_path = os.path.join(output_dir, "outputApplyingThemesInChart.xlsx")
    workbook.save(output_path)

    print("ApplyingThemesInChart executed successfully.")

if __name__ == "__main__":
    run_applying_themes_in_chart()