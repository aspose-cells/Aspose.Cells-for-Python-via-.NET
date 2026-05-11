class ColumnDetector:

    def detect_numeric_columns(self, sheet):
        numeric_columns = []

        max_col = sheet.cells.max_data_column
        max_row = sheet.cells.max_data_row

        for col in range(max_col + 1):
            numeric_count = 0

            for row in range(1, max_row + 1):
                value = sheet.cells.get(row, col).value

                if isinstance(value, (int, float)):
                    numeric_count += 1

            if numeric_count > 0:
                numeric_columns.append(col)

        return numeric_columns