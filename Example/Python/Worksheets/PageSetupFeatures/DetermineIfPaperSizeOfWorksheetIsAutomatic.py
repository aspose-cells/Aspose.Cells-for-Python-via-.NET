import os
from pathlib import Path
from datetime import datetime
from aspose import pydrawing
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "DetermineIfPaperSizeOfWorksheetIsAutomatic"


def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    wb1 = cells.Workbook(os.path.join(source_dir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"))
    wb2 = cells.Workbook(os.path.join(source_dir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"))

    ws11 = wb1.worksheets[0]
    ws12 = wb2.worksheets[0]

    print(f"First Worksheet of First Workbook - IsAutomaticPaperSize: {ws11.page_setup.is_automatic_paper_size}")
    print(f"First Worksheet of Second Workbook - IsAutomaticPaperSize: {ws12.page_setup.is_automatic_paper_size}")

    print()
    print("DetermineIfPaperSizeOfWorksheetIsAutomatic executed successfully.\r\n")


if __name__ == "__main__":
    main()