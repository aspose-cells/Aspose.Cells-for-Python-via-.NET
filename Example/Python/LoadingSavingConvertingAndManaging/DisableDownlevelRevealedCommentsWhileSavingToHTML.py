import os
from aspose.cells import Workbook, HtmlSaveOptions
from datetime import datetime
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def disable_downlevel_revealed_comments_while_saving_to_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample workbook
    wb = Workbook(str(source_dir / "sampleDisableDownlevelRevealedComments.xlsx"))
    
    # Disable DisableDownlevelRevealedComments
    opts = HtmlSaveOptions()
    opts.disable_downlevel_revealed_comments = True
    
    # Save the workbook in html
    wb.save(str(output_dir / "outputDisableDownlevelRevealedComments_true.html"), opts)
    
    print("DisableDownlevelRevealedCommentsWhileSavingToHTML executed successfully.\r\n")

if __name__ == "__main__":
    disable_downlevel_revealed_comments_while_saving_to_html()