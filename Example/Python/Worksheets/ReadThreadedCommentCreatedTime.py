import os
from pathlib import Path
from datetime import datetime
from aspose import cells
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/ReadThreadedCommentCreatedTime"

def run():
    source_dir = str(get_source_directory())
    data_dir = str(get_data_dir())
    
    # Ensure data directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    workbook = Workbook(os.path.join(source_dir, "ThreadedCommentsSample.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    threaded_comments = worksheet.comments.get_threaded_comments("A1")
    
    for comment in threaded_comments:
        print("Comment: " + comment.notes)
        print("Author: " + comment.author.name)
        print("Created Time: " + str(comment.created_time))
    
    print("ReadThreadedCommentCreatedTime executed successfully.")

if __name__ == "__main__":
    run()