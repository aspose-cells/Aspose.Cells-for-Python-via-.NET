import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook, XmlMap
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "XmlMaps/QueryCellAreasMappedToXmlMapPath"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample Excel file having Xml Map
    wb = Workbook(str(source_dir / "sampleXmlMapQuery.xlsx"))
    
    # Access first XML Map
    xmap = wb.worksheets.xml_maps[0]
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Query Xml Map from Path - /MiscData
    print("Query Xml Map from Path - /MiscData")
    ret = ws.xml_map_query("/MiscData", xmap)
    
    # Print returned ArrayList values
    for i in range(len(ret)):
        print(ret[i])
    
    print("")
    
    # Query Xml Map from Path - /MiscData/row/Color
    print("Query Xml Map from Path - /MiscData/row/Color")
    ret = ws.xml_map_query("/MiscData/row/Color", xmap)
    
    # Print returned ArrayList values
    for i in range(len(ret)):
        print(ret[i])
    
    print("QueryCellAreasMappedToXmlMapPath executed successfully.\r\n")

if __name__ == "__main__":
    run()