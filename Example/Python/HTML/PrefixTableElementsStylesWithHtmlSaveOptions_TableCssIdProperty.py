import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_prefix_table_elements_styles_with_html_save_options_table_css_id_property():
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

    # Specify html save options - specify table css id
    opts = cells.HtmlSaveOptions()
    opts.table_css_id = "MyTest_TableCssId"

    # Save the workbook in html
    output_path = os.path.join(output_dir, "outputTableCssId.html")
    workbook.save(output_path, opts)

    print("PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty executed successfully.")


if __name__ == "__main__":
    run_prefix_table_elements_styles_with_html_save_options_table_css_id_property()