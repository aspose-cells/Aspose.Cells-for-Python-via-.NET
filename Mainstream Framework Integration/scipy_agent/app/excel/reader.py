import aspose.cells as cells
import pandas as pd


class ExcelReader:

    @staticmethod
    def load_sheet_as_dataframe(file_path, sheet_index=0):
        workbook = cells.Workbook(file_path)
        worksheet = workbook.worksheets[sheet_index]

        rows = worksheet.cells.max_data_row + 1
        cols = worksheet.cells.max_data_column + 1

        data = []

        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(worksheet.cells.get(r, c).value)
            data.append(row)

        df = pd.DataFrame(data[1:], columns=data[0])
        return df