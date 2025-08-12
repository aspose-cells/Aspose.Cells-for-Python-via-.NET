import locale
import os
import io
import logging
from typing import Any, BinaryIO

from markitdown import (
    DocumentConverter,
    DocumentConverterResult,
    MarkItDown,
    StreamInfo,
)

from aspose.cells import Workbook,MarkdownSaveOptions,License,SaveFormat

__plugin_interface_version__ = (
    1  # The version of the plugin interface that this plugin uses
)

ACCEPTED_MIME_TYPE_PREFIXES = [
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
    "application/vnd.ms-excel",                                           # .xls
    "application/vnd.oasis.opendocument.spreadsheet",                     # .ods
]

ACCEPTED_FILE_EXTENSIONS = [".xlsx",".xls",".ods"]


def register_converters(markitdown: MarkItDown, **kwargs):
    """
    Called during construction of MarkItDown instances to register converters provided by plugins.
    """
    markitdown.register_converter(AsposeCellsConverter())

    # E,g. for Windows:
    # PowerShell£º$env:ASPOSE_LICENSE_PATH = "D:\Files\Aspose.Cells.lic"
    # CDM£º       set ASPOSE_LICENSE_PATH=D:\Files\Aspose.Cells.lic
class LicenseManager:
    def __init__(self):
        self.license_path = os.getenv("ASPOSE_LICENSE_PATH")

    def apply_license(self):
        # logging.warning(self.license_path)
        if self.license_path and os.path.exists(self.license_path):
            logging.info(f"Applying Aspose license from: {self.license_path}")
            lic = License()
            lic.set_license(self.license_path)

        else:
            logging.warning("No valid Aspose license found.Running in free mode.Please set the ASPOSE_LICENSE_PATH environment variable.")


class AsposeCellsConverter(DocumentConverter):
    """
    Converts an Excel file to in the simplest possible way.
    """

    def accepts(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,
    ) -> bool:
        mimetype = (stream_info.mimetype or "").lower()
        extension = (stream_info.extension or "").lower()

        if extension in ACCEPTED_FILE_EXTENSIONS:
            return True

        for prefix in ACCEPTED_MIME_TYPE_PREFIXES:
            if mimetype.startswith(prefix):
                return True

        return False

    def convert(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,
    ) -> DocumentConverterResult:
        LicenseManager().apply_license()
        workbook = Workbook(file_stream)
        out_stream = io.BytesIO()
        opt = MarkdownSaveOptions()
        # Set other properties
        # ...
        workbook.save(out_stream, opt)
        textStr = out_stream.getvalue().decode('utf-8')
        return DocumentConverterResult(
            title=None,
            markdown=textStr,
        )

