import os
import sys
from pathlib import Path
from datetime import datetime

import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "XmlMaps/FindRootElementNameOfXmlMap"

def run():
    source_dir = get_source_directory()
    
    wb = cells.Workbook(str(source_dir / "sampleRootElementNameOfXmlMap.xlsx"))
    
    xmap = wb.worksheets.xml_maps[0]
    
    print("Root Element Name Of Xml Map: " + xmap.root_element_name)
    
    print("FindRootElementNameOfXmlMap executed successfully.\r\n")

if __name__ == "__main__":
    run()