import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

class CellsDataTable(cells.ICellsDataTable):
    def __init__(self):
        self._m_index = -1
        self._cols_names = ["Pet", "Fruit", "Country", "Color"]
        self._col0data = ["Dog", "Cat", "Duck"]
        self._col1data = ["Apple", "Pear", "Banana"]
        self._col2data = ["UK", "USA", "China"]
        self._col3data = ["Red", "Green", "Blue"]
        self._cols_data = [
            self._col0data,
            self._col1data,
            self._col2data,
            self._col3data,
        ]

    # ICellsDataTable indexer
    def get_Item(self, column_index):
        return self._cols_data[column_index][self._m_index]

    # support Pythonic indexing as well
    def __getitem__(self, column_index):
        return self.get_Item(column_index)

    # ICellsDataTable.Columns property
    @property
    def columns(self):
        return self._cols_names

    # ICellsDataTable.Count property
    @property
    def count(self):
        return len(self._col0data)

    # ICellsDataTable.BeforeFirst method
    def before_first(self):
        self._m_index = -1

    # ICellsDataTable.Next method (lower‑case name expected by the abstract base)
    def next(self):
        self._m_index += 1
        return True

    # also provide the Pascal‑case name for safety
    def BeforeFirst(self):
        self.before_first()

    def Next(self):
        return self.next()

def run_shift_first_row_down_when_inserting_cells_data_table_rows():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # ensure output directory exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    data_table = CellsDataTable()

    workbook_path = os.path.join(source_dir, "sampleImportTableOptionsShiftFirstRowDown.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]

    options = cells.ImportTableOptions()
    options.shift_first_row_down = False

    worksheet.cells.import_data(data_table, 2, 2, options)

    output_path = os.path.join(output_dir, "outputImportTableOptionsShiftFirstRowDown-False.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    run_shift_first_row_down_when_inserting_cells_data_table_rows()