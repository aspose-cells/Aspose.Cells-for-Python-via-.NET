import os
from pathlib import Path
from aspose.cells import Workbook
from datetime import datetime


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"


def main():
    source_dir = get_source_directory()
    file_path = os.path.join(source_dir, "ThreadedCommentsSample.xlsx")
    
    workbook = Workbook(file_path)
    
    worksheet = workbook.worksheets[0]
    
    threaded_comments = worksheet.comments.get_threaded_comments("A1")
    
    for comment in threaded_comments:
        print(f"Comment: {comment.notes}")
        print(f"Author: {comment.author.name}")
    
    print("ReadThreadedComments executed successfully.")


if __name__ == "__main__":
    main()