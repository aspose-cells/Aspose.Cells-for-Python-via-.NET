import os
import aspose.cells as cells
from aspose.cells.rendering import  IPageSavingCallback,PageStartSavingArgs,PageStartSavingArgs,PageEndSavingArgs

def get_source_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "01_SourceDirectory")


def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")


class TestPageSavingCallback(IPageSavingCallback):
    def page_start_saving(self, args: PageStartSavingArgs):
        print(f"Start saving page index {args.page_index} of pages {args.page_count}")
        if args.page_index < 2:
            args.is_to_output = False

    def page_end_saving(self, args: PageEndSavingArgs):
        print(f"End saving page index {args.page_index} of pages {args.page_count}")
        if args.page_index >= 8:
            args.has_more_pages = False


def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = cells.Workbook(os.path.join(source_dir, "PagesBook1.xlsx"))

    pdf_save_options = cells.PdfSaveOptions()
    pdf_save_options.page_saving_callback = TestPageSavingCallback()

    workbook.save(os.path.join(output_dir, "DocumentConversionProgress.pdf"), pdf_save_options)

    print("DocumentConversionProgress executed successfully.")


if __name__ == "__main__":
    run()