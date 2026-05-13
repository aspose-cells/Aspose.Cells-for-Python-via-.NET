import aspose.cells as cells

class ExcelWriter:

    @staticmethod
    def write_report(output_path, reports):

        workbook = cells.Workbook()
        sheet = workbook.worksheets[0]

        row = 0

        for key, value in reports.items():
            sheet.cells.get(row, 0).put_value(str(key))
            sheet.cells.get(row, 1).put_value(str(value))
            row += 1

        workbook.save(output_path)