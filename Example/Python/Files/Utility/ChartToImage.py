import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Utility" / "ChartToImage"


def run():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    workbook = cells.Workbook()
    sheet_index = workbook.worksheets.add()
    worksheet = workbook.worksheets[sheet_index]

    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("B1").put_value(4)
    worksheet.cells.get("B2").put_value(20)
    worksheet.cells.get("B3").put_value(50)

    chart_index = worksheet.charts.add(cells.charts.ChartType.COLUMN, 5, 0, 15, 5)
    chart = worksheet.charts[chart_index]
    chart.n_series.add("A1:B3", True)

    chart.to_image(str(data_dir / "Chart.emf"))
    print("Image generated successfully.")


if __name__ == "__main__":
    run()
