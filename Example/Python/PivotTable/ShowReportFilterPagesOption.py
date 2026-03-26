import os
import aspose.cells as cells

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load template file
    wb = cells.Workbook(os.path.join(source_dir, "samplePivotTable.xlsx"))

    # Get first pivot table in the worksheet
    pt = wb.worksheets[1].pivot_tables[0]

    # Set pivot field
    pt.show_report_filter_page(pt.page_fields[0])

    # Set position index for showing report filter pages
    pt.show_report_filter_page_by_index(pt.page_fields[0].position)

    # Set the page field name
    pt.show_report_filter_page_by_name(pt.page_fields[0].name)

    # Save the output file
    wb.save(os.path.join(output_dir, "outputSamplePivotTable.xlsx"))

if __name__ == "__main__":
    main()