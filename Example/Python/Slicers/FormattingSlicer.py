import os
import aspose.cells as cells

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load sample Excel file containing slicer.
    wb = cells.Workbook(os.path.join(source_dir, "sampleFormattingSlicer.xlsx"))

    # Access first worksheet.
    ws = wb.worksheets[0]

    # Access the first slicer inside the slicer collection.
    slicer = ws.slicers[0]

    # Set the number of columns of the slicer.
    slicer.number_of_columns = 2

    # Set the type of slicer style.
    slicer.style_type = cells.slicers.SlicerStyleType.SLICER_STYLE_LIGHT6

    # Save the workbook in output XLSX format.
    wb.save(os.path.join(output_dir, "outputFormattingSlicer.xlsx"))

    print("FormattingSlicer executed successfully.")

if __name__ == "__main__":
    main()