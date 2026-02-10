import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Utility" / "EncryptingFiles").resolve()


def run():
    # ExStart:1
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))

    # Specify XOR encryption type.
    workbook.set_encryption_options(cells.EncryptionType.XOR, 40)

    # Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
    workbook.set_encryption_options(cells.EncryptionType.StrongCryptographicProvider, 128)

    # Password protect the file.
    workbook.settings.password = "1234"

    # Save the excel file.
    workbook.save(str(data_dir / "encryptedBook1.out.xls"))
    # ExEnd:1


def specify_password_to_modify_option():
    # ExStart:SpecifyPasswordToModifyOption
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))

    # Set the password for modification.
    workbook.settings.write_protection.password = "1234"

    # Save the excel file.
    workbook.save(str(data_dir / "SpecifyPasswordToModifyOption.out.xls"))
    # ExEnd:SpecifyPasswordToModifyOption