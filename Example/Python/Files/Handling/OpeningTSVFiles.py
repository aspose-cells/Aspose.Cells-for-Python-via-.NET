import aspose.cells as cells
import io


def main():
    tsv_data = (
        "A1\tB1\tC1\n"
        "A2\tB2\tC2\n"
        "A3\tB3\tC3"
    )
    stream = io.BytesIO(tsv_data.encode("utf-8"))

    load_options = cells.LoadOptions(cells.LoadFormat.TSV)
    workbook = cells.Workbook(stream, load_options)

    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get("C3")

    print(f"Cell Name: {cell.name} Value: {cell.string_value}")
    print("OpeningTSVFiles executed successfully!")


if __name__ == "__main__":
    main()