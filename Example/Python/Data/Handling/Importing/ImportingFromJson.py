import os
import aspose.cells as cells
import aspose.cells.utility as utility
from aspose.pydrawing import Color

def get_data_directory():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "Data"))

def run_importing_from_json():
    data_dir = get_data_directory()
    json_path = os.path.join(data_dir, "Test.json")

    if not os.path.isfile(json_path):
        sample_json = """{
    "Employees": [
        {"Name": "John Doe", "Age": 30},
        {"Name": "Jane Smith", "Age": 25}
    ]
}"""
        os.makedirs(data_dir, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(sample_json)

    with open(json_path, "r", encoding="utf-8") as f:
        json_input = f.read()

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    factory = cells.CellsFactory()
    style = factory.create_style()
    style.horizontal_alignment = cells.TextAlignmentType.CENTER
    style.font.color = Color.blue_violet
    style.font.is_bold = True

    options = utility.JsonLayoutOptions()
    options.title_style = style
    options.array_as_table = True

    utility.JsonUtility.import_data(json_input, worksheet.cells, 0, 0, options)

    output_path = os.path.join(data_dir, "ImportingFromJson.out.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_json()
