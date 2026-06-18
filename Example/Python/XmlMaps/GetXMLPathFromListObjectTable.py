import os
from pathlib import Path
from aspose.cells import Workbook

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    source_dir = os.path.join(str(get_source_directory()), "SampleXmlData")
    
    workbook = Workbook(os.path.join(source_dir, "XML Data.xlsx"))
    
    ws = workbook.worksheets[0]
    
    list_object = ws.list_objects[0]
    
    url = list_object.xml_map.data_binding.url
    
    print(url)
    
    print("GetXMLPathFromListObjectTable executed successfully.\r\n")

if __name__ == "__main__":
    main()