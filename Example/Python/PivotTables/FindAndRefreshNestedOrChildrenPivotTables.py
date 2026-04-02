import os
from pathlib import Path
from aspose import cells
from aspose.cells import Workbook
from aspose.cells.pivot import PivotTable

def get_source_directory(): 
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    source_dir = str(get_source_directory())
    
    # Load sample Excel file
    wb = Workbook(os.path.join(source_dir, "sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx"))
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Access third pivot table
    pt_parent = ws.pivot_tables[2]
    
    # Access the children of the parent pivot table
    pt_children = pt_parent.get_children()
    
    # Refresh all the children pivot tables
    for pt_child in pt_children:
        pt_child.refresh_data()
        pt_child.calculate_data()
    
    print("FindAndRefreshNestedOrChildrenPivotTables executed successfully.")

if __name__ == "__main__":
    main()