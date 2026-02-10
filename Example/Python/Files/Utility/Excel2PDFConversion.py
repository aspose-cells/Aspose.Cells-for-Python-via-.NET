from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Utility/Excel2PDFConversion"

def run():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "abc.xlsx"))
    workbook.save(str(data_dir / "outBook2.out.pdf"), cells.SaveFormat.PDF)
    print("Conversion completed.")

if __name__ == "__main__":
    run()