import os
from aspose.cells import Workbook, PdfSaveOptions
from aspose.cells.rendering import PdfBookmarkEntry
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Rendering/AddPDFBookmarksWithNamedDestinations"


def run():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())

    # Load source Excel file
    wb = Workbook(os.path.join(source_dir, "samplePdfBookmarkEntry_DestinationName.xlsx"))

    # Access first worksheet
    ws = wb.worksheets[0]

    # Access cell C5
    cell = ws.cells.get("C5")

    # Create Bookmark and Destination for this cell
    bookmark_entry = PdfBookmarkEntry()
    bookmark_entry.text = "Text"
    bookmark_entry.destination = cell
    bookmark_entry.destination_name = "AsposeCells--" + cell.name

    # Access cell G56
    cell = ws.cells.get("G56")

    # Create Sub-Bookmark and Destination for this cell
    subbookmark_entry1 = PdfBookmarkEntry()
    subbookmark_entry1.text = "Text1"
    subbookmark_entry1.destination = cell
    subbookmark_entry1.destination_name = "AsposeCells--" + cell.name

    # Access cell L4
    cell = ws.cells.get("L4")

    # Create Sub-Bookmark and Destination for this cell
    subbookmark_entry2 = PdfBookmarkEntry()
    subbookmark_entry2.text = "Text2"
    subbookmark_entry2.destination = cell
    subbookmark_entry2.destination_name = "AsposeCells--" + cell.name

    # Add Sub-Bookmarks in list
    bookmark_list = [subbookmark_entry1, subbookmark_entry2]

    # Assign Sub-Bookmarks list to Bookmark Sub-Entry
    bookmark_entry.sub_entry = bookmark_list

    # Create PdfSaveOptions and assign Bookmark to it
    opts = PdfSaveOptions()
    opts.bookmark = bookmark_entry

    # Save the workbook in Pdf format with given pdf save options
    wb.save(os.path.join(output_dir, "outputPdfBookmarkEntry_DestinationName.pdf"), opts)


if __name__ == "__main__":
    run()