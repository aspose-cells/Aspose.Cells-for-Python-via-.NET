import os
from datetime import datetime
from pathlib import Path
from aspose import pydrawing as drawing
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/ConvertTableToOds"

def run():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())

    # Open an existing file that contains a table/list object in it
    wb = cells.Workbook(os.path.join(source_dir, "SampleTable.xlsx"))

    # Save the file
    wb.save(os.path.join(output_dir, "ConvertTableToOds_out.ods"))

    print("ConvertTableToOds executed successfully.")

if __name__ == "__main__":
    run()