import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

class MyStreamProvider(cells.IStreamProvider):
    def close_stream(self, options):
        pass

    def init_stream(self, options):
        source_dir = get_source_directory()
        image_path = os.path.join(str(source_dir), "newPdfSaveOptions_StreamProvider.png")
        with open(image_path, "rb") as f:
            data = f.read()
        options.stream = cells.io.MemoryStream(data)

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    os.makedirs(str(output_dir), exist_ok=True)
    
    wb = cells.Workbook(os.path.join(str(source_dir), "samplePdfSaveOptions_StreamProvider.xlsx"))
    
    opts = cells.PdfSaveOptions()
    opts.one_page_per_sheet = True
    
    wb.settings.stream_provider = MyStreamProvider()
    
    output_path = os.path.join(str(output_dir), "outputPdfSaveOptions_StreamProvider.pdf")
    wb.save(output_path, opts)

if __name__ == "__main__":
    main()