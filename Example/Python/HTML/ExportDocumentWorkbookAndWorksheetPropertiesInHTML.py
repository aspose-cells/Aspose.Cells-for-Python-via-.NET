import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_export_document_workbook_and_worksheet_properties_in_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx")
    workbook = cells.Workbook(workbook_path)

    options = cells.HtmlSaveOptions()
    options.export_document_properties = False
    options.export_workbook_properties = False
    options.export_worksheet_properties = False

    output_path = os.path.join(output_dir, "outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html")
    workbook.save(output_path, options)

    print("ExportDocumentWorkbookAndWorksheetPropertiesInHTML executed successfully.")

if __name__ == "__main__":
    run_export_document_workbook_and_worksheet_properties_in_html()