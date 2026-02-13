import os
import tempfile
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Handling"
        / "SaveWorkbookToTextCSVFormat"
    ).resolve()


def run():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "book1.xls"))

    combined_data = bytearray()
    opts = cells.TxtSaveOptions()
    opts.separator = "\t"

    for idx in range(len(workbook.worksheets)):
        workbook.worksheets.active_sheet_index = idx

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_path = tmp_file.name

        workbook.save(tmp_path, opts)
        combined_data.extend(Path(tmp_path).read_bytes())
        os.remove(tmp_path)

    (data_dir / "out.txt").write_bytes(combined_data)


if __name__ == "__main__":
    run()
