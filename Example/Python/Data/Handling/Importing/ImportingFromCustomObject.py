import os
import aspose.cells as cells

def get_data_dir():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "03_DataDirectory"))

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self, value):
        self._age = value

def run_importing_from_custom_object():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]

    # Prepare data
    persons = [
        Person("Mike", 25),
        Person("Steve", 30),
        Person("Billy", 35)
    ]

    # Write header
    sheet.cells.get(0, 0).put_value("Name")
    sheet.cells.get(0, 1).put_value("Age")

    # Write data rows
    for i, p in enumerate(persons, start=1):
        sheet.cells.get(i, 0).put_value(p.Name)
        sheet.cells.get(i, 1).put_value(p.Age)

    # Auto‑fit columns
    sheet.auto_fit_columns()

    output_path = os.path.join(data_dir, "ImportedCustomObjects.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_custom_object()
