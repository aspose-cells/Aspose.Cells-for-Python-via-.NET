import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Comments" / "AddImageToComment"

def run_add_image_to_comment():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    comments = workbook.worksheets[0].comments

    comment_index = comments.add(0, 0)
    comment = comments[comment_index]
    comment.note = "First note."
    comment.font.name = "Times New Roman"

    image_path = os.path.join(data_dir, "logo.jpg")
    with open(image_path, "rb") as f:
        img_bytes = f.read()

    comment.comment_shape.fill.image_data = img_bytes

    output_path = os.path.join(data_dir, "book1.out.xlsx")
    workbook.save(output_path, cells.SaveFormat.XLSX)

if __name__ == "__main__":
    run_add_image_to_comment()