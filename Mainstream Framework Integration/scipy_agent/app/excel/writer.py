import aspose.cells as cells


class ExcelWriter:

    def save(self, workbook, output_path: str):
        workbook.save(output_path)

    def add_summary_sheet(self, workbook, text: str):
        index = workbook.worksheets.add()
        sheet = workbook.worksheets[index]
        sheet.name = "Summary"

        sheet.cells.get("A1").put_value(text)