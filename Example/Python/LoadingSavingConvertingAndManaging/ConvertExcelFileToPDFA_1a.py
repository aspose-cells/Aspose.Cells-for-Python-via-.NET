import os
from pathlib import Path
from aspose.cells import Workbook, PdfSaveOptions
from aspose.cells.rendering import PdfCompliance

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    wb = Workbook()
    ws = wb.worksheets[0]
    cell = ws.cells.get("B5")
    cell.put_value("This PDF format is compatible with PDFA-1a.")
    
    opts = PdfSaveOptions()
    opts.compliance = PdfCompliance.PDF_A1A
    
    output_path = os.path.join(output_dir, "outputCompliancePdfA1a.pdf")
    wb.save(output_path, opts)

if __name__ == "__main__":
    main()