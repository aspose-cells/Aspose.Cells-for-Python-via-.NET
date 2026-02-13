from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "SaveXLSXFile"

def run():
    data_dir = get_data_dir()
    response = None
    workbook = cells.Workbook()
    if response is not None:
        workbook.save(response, str(data_dir / "output.xlsx"), cells.ContentDisposition.ATTACHMENT, cells.OoxmlSaveOptions())
        response.end()

if __name__ == "__main__":
    run()