import aspose.cells as cells
import os
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Utility/EncryptingODSFiles"


def run():
    data_dir = get_data_dir()

    # Open the ODS file.
    workbook = cells.Workbook(str(data_dir / "Book1.ods"))

    # Password protect the file.
    workbook.settings.password = "1234"

    # Save the encrypted ODS file.
    workbook.save(str(data_dir / "encryptedBook1.out.ods"))

    # Load the encrypted ODS file with the appropriate load options.
    load_options = cells.OdsLoadOptions()
    load_options.password = "1234"
    encrypted = cells.Workbook(str(data_dir / "encryptedBook1.out.ods"), load_options)

    # Unprotect the workbook.
    encrypted.unprotect("1234")

    # Remove the password.
    encrypted.settings.password = None

    # Save the decrypted ODS file.
    encrypted.save(str(data_dir / "DencryptedBook1.out.ods"))


if __name__ == "__main__":
    run()