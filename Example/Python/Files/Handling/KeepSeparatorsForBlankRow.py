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
        / "KeepSeparatorsForBlankRow"
    ).resolve()


def main():
    data_dir = get_data_dir()
    file_path = data_dir / "Book1.xlsx"

    wb = cells.Workbook(str(file_path))

    options = cells.TxtSaveOptions()
    options.keep_separators_for_blank_row = True

    output_path = data_dir / "output.csv"
    wb.save(str(output_path), options)

    print("KeepSeparatorsForBlankRow executed successfully.\r\n")


if __name__ == "__main__":
    main()