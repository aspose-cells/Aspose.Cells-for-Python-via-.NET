import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


class TextParser(cells.ICustomParser):
    def parse_object(self, value):
        return value

    def get_format(self):
        return ""


class DateParser(cells.ICustomParser):
    def parse_object(self, value):
        return datetime.strptime(value, "%d/%m/%Y")

    def get_format(self):
        return "dd/MM/yyyy"


def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    txt_load_options = cells.TxtLoadOptions(cells.LoadFormat.CSV)
    txt_load_options.separator = ","
    txt_load_options.encoding = "utf-8"
    txt_load_options.convert_date_time_data = True
    txt_load_options.preferred_parsers = [TextParser(), DateParser()]

    workbook = cells.Workbook(str(source_dir / "samplePreferredParser.csv"), txt_load_options)

    cell = workbook.worksheets[0].cells.get("A1")
    print(f"A1: {cell.type} - {cell.display_string_value}")

    cell = workbook.worksheets[0].cells.get("B1")
    print(f"B1: {cell.type} - {cell.display_string_value}")

    workbook.save(str(output_dir / "outputsamplePreferredParser.xlsx"))
    print("OpeningCSVFilesWithPreferredParser executed successfully.\r\n")


if __name__ == "__main__":
    main()
