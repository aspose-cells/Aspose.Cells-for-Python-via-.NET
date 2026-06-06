import os
from datetime import datetime
from aspose import pydrawing
from aspose.cells import Workbook, CommentCollection
from pathlib import Path


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"


def run():
    source_dir = get_source_directory()
    out_dir = get_output_directory()

    workbook = Workbook(str(source_dir / "ThreadedCommentsSample.xlsx"))

    worksheet = workbook.worksheets[0]
    comments = worksheet.comments

    author = worksheet.comments.get_threaded_comments("A1")[0].author

    comments.remove_at("A1")

    authors = workbook.worksheets.threaded_comment_authors

    workbook.save(str(out_dir / "ThreadedCommentsSample_Out.xlsx"))

    print("RemoveThreadedComments executed successfully.")


if __name__ == "__main__":
    run()