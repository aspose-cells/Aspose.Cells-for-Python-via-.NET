import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_get_odata_details():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "ODataSample.xlsx")
    workbook = cells.Workbook(workbook_path)

    pqf_collection = workbook.data_mashup.power_query_formulas
    for pqf in pqf_collection:
        print(f"Connection Name: {pqf.name}")
        pqfi_collection = pqf.power_query_formula_items
        for pqfi in pqfi_collection:
            print(f"Name: {pqfi.name}")
            print(f"Value: {pqfi.value}")

    print("GetOdataDetails executed successfully.")

if __name__ == "__main__":
    run_get_odata_details()
