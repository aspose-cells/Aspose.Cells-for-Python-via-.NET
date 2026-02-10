import os
from pathlib import Path
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def run():
    source_dir = get_source_directory()
    filename = source_dir / "encryptedBook1.out.tmp"

    with open(str(filename), "rb") as stream:
        file_format_info = cells.FileFormatUtil.detect_file_format(stream, "1234")

    print("File Format:", file_format_info.file_format_type)


if __name__ == "__main__":
    run()