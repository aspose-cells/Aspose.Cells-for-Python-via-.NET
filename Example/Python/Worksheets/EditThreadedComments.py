import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/EditThreadedComments"

def run():
    source_dir = str(get_source_directory())
    out_dir = str(get_output_directory())

    workbook = Workbook(os.path.join(source_dir, "ThreadedCommentsSample.xlsx"))

    worksheet = workbook.worksheets[0]

    comment = worksheet.comments.get_threaded_comments("A1")[0]
    comment.notes = "Updated Comment"

    workbook.save(os.path.join(out_dir, "EditThreadedComments.xlsx"))

if __name__ == "__main__":
    run()