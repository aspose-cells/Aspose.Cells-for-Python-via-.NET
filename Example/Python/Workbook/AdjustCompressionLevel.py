import os
import time
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_adjust_compression_level():
    source_dir = get_source_directory()
    out_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "LargeSampleFile.xlsx")
    workbook = cells.Workbook(workbook_path)

    options = cells.XlsbSaveOptions()

    # Level 1
    options.compression_type = cells.OoxmlCompressionType.LEVEL1
    start = time.perf_counter()
    workbook.save(os.path.join(out_dir, "LargeSampleFile_level_1_out.xlsb"), options)
    elapsed_ms = int((time.perf_counter() - start) * 1000)
    print(f"Level 1 Elapsed Time: {elapsed_ms}")

    # Level 6
    options.compression_type = cells.OoxmlCompressionType.LEVEL6
    start = time.perf_counter()
    workbook.save(os.path.join(out_dir, "LargeSampleFile_level_6_out.xlsb"), options)
    elapsed_ms = int((time.perf_counter() - start) * 1000)
    print(f"Level 6 Elapsed Time: {elapsed_ms}")

    # Level 9
    options.compression_type = cells.OoxmlCompressionType.LEVEL9
    start = time.perf_counter()
    workbook.save(os.path.join(out_dir, "LargeSampleFile_level_9_out.xlsb"), options)
    elapsed_ms = int((time.perf_counter() - start) * 1000)
    print(f"Level 9 Elapsed Time: {elapsed_ms}")

    print("AdjustCompressionLevel executed successfully.")

if __name__ == "__main__":
    run_adjust_compression_level()