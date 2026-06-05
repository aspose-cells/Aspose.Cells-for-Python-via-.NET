from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path
from datetime import datetime

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    out_dir = str(get_output_directory())
    
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    
    workbook = Workbook()
    
    # Add Author
    author_index = workbook.worksheets.threaded_comment_authors.add("Aspose Test", "", "")
    author = workbook.worksheets.threaded_comment_authors[author_index]
    
    # Add Threaded Comment
    workbook.worksheets[0].comments.add_threaded_comment("A1", "Test Threaded Comment", author)
    
    output_path = os.path.join(out_dir, "AddThreadedComments_out.xlsx")
    workbook.save(output_path)
    
    print("AddThreadedComments executed successfully.")

if __name__ == "__main__":
    main()