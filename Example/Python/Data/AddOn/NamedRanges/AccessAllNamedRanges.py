import os
import aspose.cells as cells

def get_source_directory():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur_dir, "Data", "01_SourceDirectory")
        if os.path.isdir(candidate):
            return candidate
        parent_dir = os.path.abspath(os.path.join(cur_dir, os.pardir))
        if parent_dir == cur_dir:
            # Reached filesystem root; return the last candidate even if it doesn't exist
            return candidate
        cur_dir = parent_dir

def run_access_all_named_ranges():
    source_dir = get_source_directory()
    input_path = os.path.join(source_dir, "sampleAccessAllNamedRanges.xlsx")
    workbook = cells.Workbook(input_path)
    ranges = workbook.worksheets.get_named_ranges()
    print("Total Number of Named Ranges: " + str(len(ranges)))
    print("AccessAllNamedRanges executed successfully.")

if __name__ == "__main__":
    run_access_all_named_ranges()