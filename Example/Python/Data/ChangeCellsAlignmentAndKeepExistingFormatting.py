import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_change_cells_alignment_and_keep_existing_formatting():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]

    rng = worksheet.cells.create_range("B2:D7")

    style = workbook.create_style()
    style.horizontal_alignment = cells.TextAlignmentType.CENTER
    style.vertical_alignment = cells.TextAlignmentType.CENTER

    flag = cells.StyleFlag()
    flag.alignments = True

    rng.apply_style(style, flag)

    output_file = os.path.join(output_dir, "outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx")
    workbook.save(output_file, cells.SaveFormat.XLSX)

    print("ChangeCellsAlignmentAndKeepExistingFormatting executed successfully.")

if __name__ == "__main__":
    run_change_cells_alignment_and_keep_existing_formatting()