import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return (Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory").resolve()

def get_output_directory():
    return (Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory").resolve()

def sheet_replace(workbook: cells.Workbook, s_find: str, s_replace: str):
    finding = s_find

    # Replace in sheet cells, headers and footers
    for sheet in workbook.worksheets:
        sheet.replace(finding, s_replace)

        for j in range(3):
            header = sheet.page_setup.get_header(j)
            if header is not None:
                sheet.page_setup.set_header(j, header.replace(finding, s_replace))

            footer = sheet.page_setup.get_footer(j)
            if footer is not None:
                sheet.page_setup.set_footer(j, footer.replace(finding, s_replace))

    # Replace in text boxes
    escaped_find = s_find.replace("<", "&lt;").replace(">", "&gt;")
    for sheet in workbook.worksheets:
        for textbox in sheet.text_boxes:
            if textbox.html_text and escaped_find in textbox.html_text:
                textbox.html_text = textbox.html_text.replace(escaped_find, s_replace)

def run_replace_tag_with_text_in_textbox():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleReplaceTagWithText.xlsx")
    workbook = cells.Workbook(workbook_path)

    tag = "TAG_2$TAG_1"
    replace = "1$ys"

    tags = tag.split('$')
    replaces = replace.split('$')
    for i in range(len(tags)):
        sheet_replace(workbook, f"<{tags[i]}>", replaces[i])

    pdf_options = cells.PdfSaveOptions()
    output_path = os.path.join(output_dir, "outputReplaceTagWithText.pdf")
    workbook.save(output_path, pdf_options)

    print("ReplaceTagWithTextInTextBox executed successfully.")

if __name__ == "__main__":
    run_replace_tag_with_text_in_textbox()