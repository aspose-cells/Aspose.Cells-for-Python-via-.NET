import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_specify_language_of_excel_file_using_builtin_document_properties():
    output_dir = get_output_directory()
    workbook = cells.Workbook()
    bdpc = workbook.built_in_document_properties
    bdpc.language = "German, French"
    output_file = os.path.join(output_dir, "outputSpecifyLanguageOfExcelFileUsingBuiltinDocumentProperties.xlsx")
    workbook.save(output_file, cells.SaveFormat.XLSX)
    print("SpecifyLanguageOfExcelFileUsingBuiltinDocumentProperties executed successfully.")

if __name__ == "__main__":
    run_specify_language_of_excel_file_using_builtin_document_properties()