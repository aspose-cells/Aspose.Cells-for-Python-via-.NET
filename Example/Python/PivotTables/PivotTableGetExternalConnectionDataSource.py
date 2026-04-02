import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells


def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")


def main():
    source_dir = get_source_directory()
    
    workbook = cells.Workbook(os.path.join(source_dir, "SamplePivotTableExternalConnection.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    pivot_table = worksheet.pivot_tables[0]
    
    print("External Connection Data Source")
    print("Name: " + str(pivot_table.external_connection_data_source.name))
    print("Type: " + str(pivot_table.external_connection_data_source.type))
    
    print("PivotTableGetExternalConnectionDataSource executed successfully.")


if __name__ == "__main__":
    main()