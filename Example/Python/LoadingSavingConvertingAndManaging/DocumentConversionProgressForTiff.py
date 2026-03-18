import os
from aspose.cells import Workbook
from aspose.cells.drawing import ImageType
from aspose.cells.rendering import ImageOrPrintOptions, WorkbookRender, IPageSavingCallback, PageStartSavingArgs, PageEndSavingArgs
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

class TestTiffPageSavingCallback(IPageSavingCallback):
    def page_start_saving(self, args):
        print(f"Start saving page index {args.page_index} of pages {args.page_count}")
        if args.page_index < 2:
            args.is_to_output = False

    def page_end_saving(self, args):
        print(f"End saving page index {args.page_index} of pages {args.page_count}")
        if args.page_index >= 8:
            args.has_more_pages = False

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = Workbook(str(source_dir / "sampleUseWorkbookRenderForImageConversion.xlsx"))
    opts = ImageOrPrintOptions()
    opts.page_saving_callback = TestTiffPageSavingCallback()
    opts.image_type = ImageType.TIFF

    wr = WorkbookRender(workbook, opts)
    wr.to_image(str(output_dir / "DocumentConversionProgressForTiff_out.tiff"))

    print("DocumentConversionProgressForTiff executed successfully.")

if __name__ == "__main__":
    run()