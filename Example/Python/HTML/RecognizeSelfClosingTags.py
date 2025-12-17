import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_recognize_self_closing_tags():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Set Html load options and keep precision true
    load_options = cells.HtmlLoadOptions(cells.LoadFormat.HTML)

    # Load sample source file
    input_path = os.path.join(source_dir, "sampleSelfClosingTags.html")
    workbook = cells.Workbook(input_path, load_options)

    # Save the workbook
    output_path = os.path.join(output_dir, "outsampleSelfClosingTags.xlsx")
    workbook.save(output_path)

    print("RecognizeSelfClosingTags executed successfully.\r\n")

if __name__ == "__main__":
    run_recognize_self_closing_tags()