import os
import aspose.cells as cells
import aspose.cells.drawing as acd


def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_microsoft_theme_color_in_chart_series():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the workbook containing a chart
    input_path = os.path.join(source_dir, "sampleMicrosoftThemeColorInChartSeries.xlsx")
    workbook = cells.Workbook(input_path)

    # Access the first worksheet and its first chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Set fill type of the first series to solid
    chart.n_series[0].area.fill_format.fill_type = acd.FillType.SOLID

    # Get the CellsColor of the solid fill
    cc = chart.n_series[0].area.fill_format.solid_fill.cells_color

    # Resolve ThemeColor/ThemeColorType (may reside in different modules depending on the package version)
    try:
        ThemeColor = cells.ThemeColor
        ThemeColorType = cells.ThemeColorType
    except AttributeError:
        ThemeColor = acd.ThemeColor
        ThemeColorType = acd.ThemeColorType

    # Create a theme color (Accent6 with 60% tint) and assign it
    theme_color = ThemeColor(ThemeColorType.ACCENT6, 0.6)
    cc.theme_color = theme_color
    chart.n_series[0].area.fill_format.solid_fill.cells_color = cc

    # Save the modified workbook
    output_path = os.path.join(output_dir, "outputMicrosoftThemeColorInChartSeries.xlsx")
    workbook.save(output_path)

    print("MicrosoftThemeColorInChartSeries executed successfully.")


if __name__ == "__main__":
    run_microsoft_theme_color_in_chart_series()
