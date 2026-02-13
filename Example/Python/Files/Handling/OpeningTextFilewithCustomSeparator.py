import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/OpeningTextFilewithCustomSeparator"

data_dir = get_data_dir()
file_path = data_dir / "Book11.csv"

txt_load_options = cells.TxtLoadOptions()
txt_load_options.separator = ","
txt_load_options.encoding = "utf-8"

wb = cells.Workbook(str(file_path), txt_load_options)
wb.save(str(data_dir / "output.txt"))

print("OpeningTextFilewithCustomSeparator executed successfully.")