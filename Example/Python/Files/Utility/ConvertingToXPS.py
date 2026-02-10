import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Utility/ConvertingToXPS"


def main():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))
    sheet = workbook.worksheets[0]

    options = cells.rendering.ImageOrPrintOptions()
    options.save_format = cells.SaveFormat.XPS

    sheet_render = cells.rendering.SheetRender(sheet, options)
    sheet_render.to_image(0, str(data_dir / "out_printingxps.out.xps"))

    workbook_render = cells.rendering.WorkbookRender(workbook, options)
    workbook_render.to_image(str(data_dir / "out_whole_printingxps.out.xps"))


if __name__ == "__main__":
    main()