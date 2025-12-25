import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_regex_replace():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "SampleRegexReplace.xlsx")
    workbook = cells.Workbook(input_file)

    replace = cells.ReplaceOptions()
    replace.case_sensitive = False
    replace.match_entire_cell_contents = False
    replace.regex_key = True

    workbook.replace(r"\bKIM\b", "^^^TIM^^^", replace)

    output_file = os.path.join(output_dir, "RegexReplace_out.xlsx")
    workbook.save(output_file)

    print("RegexReplace executed successfully.")

if __name__ == "__main__":
    run_regex_replace()