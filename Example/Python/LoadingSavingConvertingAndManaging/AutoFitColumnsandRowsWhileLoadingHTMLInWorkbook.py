import os
import sys
from pathlib import Path
from aspose import pydrawing as drawing
from aspose.cells import Workbook, HtmlLoadOptions
from datetime import datetime
import io

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "LoadingSavingConvertingAndManaging/AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook"

def run():
    data_dir = get_data_dir()
    
    # Ensure output directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    # Sample HTML.
    sample_html = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>"

    # Load html string into memory stream.
    ms = io.BytesIO(sample_html.encode('utf-8'))

    # Load memory stream into workbook.
    wb = Workbook(ms)

    # Save the workbook in xlsx format.
    wb.save(str(data_dir / "outputWithout_AutoFitColsAndRows.xlsx"))

    # Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
    opts = HtmlLoadOptions()
    opts.auto_fit_cols_and_rows = True

    # Load memory stream into workbook with the above HTMLLoadOptions.
    ms.seek(0)  # Reset stream position
    wb = Workbook(ms, opts)

    # Save the workbook in xlsx format.
    wb.save(str(data_dir / "outputWith_AutoFitColsAndRows.xlsx"))

if __name__ == "__main__":
    run()