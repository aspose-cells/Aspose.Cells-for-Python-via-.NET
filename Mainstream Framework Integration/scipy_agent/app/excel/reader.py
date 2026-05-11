import aspose.cells as cells


class ExcelReader:

    def load_workbook(self, path: str):
        return cells.Workbook(path)

    def get_first_sheet(self, workbook):
        return workbook.worksheets[0]