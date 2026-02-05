import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Comments" / "AddingComment").resolve()

def run_adding_comment():
    data_dir = str(get_data_dir())

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet_index = workbook.worksheets.add()
    worksheet = workbook.worksheets[sheet_index]

    comment_index = worksheet.comments.add("F5")
    comment = worksheet.comments[comment_index]
    comment.note = "Hello Aspose!"

    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_comment()