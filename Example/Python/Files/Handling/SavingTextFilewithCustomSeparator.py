from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/SavingTextFilewithCustomSeparator"


def main():
    data_dir = get_data_dir()
    file_path = data_dir / "Book1.xlsx"

    # Create a Workbook object and open the file from its path
    wb = cells.Workbook(str(file_path))

    # Instantiate Text File's Save Options
    options = cells.TxtSaveOptions()
    # Specify the separator
    options.separator = ';'

    # Save the file with the options
    output_path = data_dir / "output.csv"
    wb.save(str(output_path), options)


if __name__ == "__main__":
    main()