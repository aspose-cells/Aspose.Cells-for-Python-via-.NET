import aspose.cells as cells
from pathlib import Path


def get_data_dir() -> Path:
    """Directory that should contain the example files."""
    return Path(__file__).parent.resolve()


def ensure_fods(file_path: Path) -> None:
    """Create a minimal FODS file if it does not exist."""
    if not file_path.is_file():
        wb = cells.Workbook()                      # empty workbook
        wb.save(str(file_path), cells.SaveFormat.FODS)


def main() -> None:
    data_dir = get_data_dir()
    fods_path = data_dir / "SampleFods.fods"

    ensure_fods(fods_path)

    workbook = cells.Workbook(str(fods_path))
    print("FODS file opened successfully!")


if __name__ == "__main__":
    main()