import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent.parent.parent / "Data" / "Files" / "Utility" / "VerifyPassword"

def run():
    file_path = get_data_dir() / "EncryptedBook1.xlsx"
    if not file_path.is_file():
        print(f"File not found: {file_path}")
        return
    with open(file_path, "rb") as stream:
        is_password_valid = cells.FileFormatUtil.verify_password(stream, "1234")
    print("Password is Valid:", is_password_valid)
    print("VerifyPassword executed successfully")

if __name__ == "__main__":
    run()
