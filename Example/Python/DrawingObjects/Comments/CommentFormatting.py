import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Comments" / "CommentFormatting"
    ).resolve()

def run_comment_formatting():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet_index = workbook.worksheets.add()
    worksheet = workbook.worksheets[sheet_index]

    comment_index = worksheet.comments.add("F5")
    comment = worksheet.comments[comment_index]

    comment.note = "Hello Aspose!"
    comment.font.size = 14               # integer (points)
    comment.font.is_bold = True
    comment.height_cm = 10.0             # double (centimeters)
    comment.width_cm = 2.0               # double (centimeters)

    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_comment_formatting()