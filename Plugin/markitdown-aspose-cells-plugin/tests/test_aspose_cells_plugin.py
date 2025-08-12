#!/usr/bin/env python3 -m pytest
import os
import pytest

from markitdown import MarkItDown, StreamInfo
from markitdown_aspose_cells_plugin import AsposeCellsConverter

TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")

ASPOSE_CELLS_TEST_STRINGS = {
    "# Sheet1",
    "",
    "|a|",
    "|---|",
    "|b|",
    "|c|",
    "|d|",
    "|e|",
    "# Evaluation Only. Created with Aspose.Cells for Python via .NET. Copyright 2003 - 2025 Aspose Pty Ltd.",
}

def test_xlsx_converter() -> None:
    """Tests the Excel converter dirctly."""
    with open(os.path.join(TEST_FILES_DIR, "test.xlsx"), "rb") as file_stream:
        converter = AsposeCellsConverter()
        result = converter.convert(
            file_stream=file_stream,
            stream_info=StreamInfo(
                mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", extension=".xlsx", filename="test.xlsx"
            ),
        )
        
        for test_string in ASPOSE_CELLS_TEST_STRINGS:
            #print(test_string)
            assert test_string in result.text_content


def test_xlsx_markitdown() -> None:
    """Tests that MarkItDown correctly loads the plugin."""
    md = MarkItDown(enable_plugins=True)
    result = md.convert(os.path.join(TEST_FILES_DIR, "test.xlsx"))

    #print(result)
    for test_string in ASPOSE_CELLS_TEST_STRINGS:
        assert test_string in result.text_content

def test_xls_converter() -> None:
    """Tests the XLS converter dirctly."""
    with open(os.path.join(TEST_FILES_DIR, "test.xls"), "rb") as file_stream:
        converter = AsposeCellsConverter()
        result = converter.convert(
            file_stream=file_stream,
            stream_info=StreamInfo(
                mimetype="application/vnd.ms-excel", extension=".xls", filename="test.xls"
            ),
        )
        
        for test_string in ASPOSE_CELLS_TEST_STRINGS:
            #print(test_string)
            assert test_string in result.text_content

def test_xls_markitdown() -> None:
    """Tests that MarkItDown correctly loads the plugin."""
    md = MarkItDown(enable_plugins=True)
    result = md.convert(os.path.join(TEST_FILES_DIR, "test.xls"))

    for test_string in ASPOSE_CELLS_TEST_STRINGS:
        assert test_string in result.text_content


if __name__ == "__main__":
    """Runs this file's tests from the command line."""
    test_xlsx_converter()
    test_xlsx_markitdown()
    test_xls_converter()
    test_xls_markitdown()
    print("All tests passed.")
