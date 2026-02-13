import os
from pathlib import Path
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def main():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())

    workbook = cells.Workbook(os.path.join(source_dir, "sampleWithCustProps.xlsx"))

    pdf_save_opt = cells.PdfSaveOptions()
    pdf_save_opt.custom_properties_export = cells.rendering.PdfCustomPropertiesExport.STANDARD

    workbook.save(os.path.join(output_dir, "outSampleWithCustProps.pdf"), pdf_save_opt)

    print("ExportCustomPropertiesToPDF executed successfully.")


if __name__ == "__main__":
    main()