import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_export_worksheet_css_separately_in_output_html():
    output_dir = get_output_directory()

    # Create workbook object
    workbook = cells.Workbook()

    # Access first worksheet
    worksheet = workbook.worksheets[0]

    # Access cell B5 and put value inside it
    cell = worksheet.cells.get("B5")
    cell.put_value("This is some text.")

    # Set the style of the cell - font color is Red
    style = cell.get_style()
    style.font.color = Color.red
    cell.set_style(style)

    # Specify HTML save options - export worksheet CSS separately
    options = cells.HtmlSaveOptions()
    options.export_worksheet_css_separately = True

    # Save the workbook in HTML
    output_file = os.path.join(output_dir, "outputExportWorksheetCSSSeparately.html")
    workbook.save(output_file, options)

    print("ExportWorksheetCSSSeparatelyInOutputHTML executed successfully.")


if __name__ == "__main__":
    run_export_worksheet_css_separately_in_output_html()