import io
import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    return Path(__file__).parent.parent.parent / "Data" / "Files" / "Utility" / "ConvertChartToPdf"


def ensure_sample_workbook(excel_path: Path) -> None:
    wb = cells.Workbook()
    ws = wb.worksheets[0]

    # Populate sample data
    for i in range(5):
        ws.cells.get(i, 0).put_value(i + 1)          # Category
        ws.cells.get(i, 1).put_value((i + 1) * 10)   # Value

    # Add a simple column chart
    chart_index = ws.charts.add(cells.charts.ChartType.COLUMN, 5, 0, 20, 5)
    chart = ws.charts[chart_index]
    chart.n_series.add("=Sheet1!$B$1:$B$5", True)

    wb.save(str(excel_path))


def run() -> None:
    data_dir = get_data_dir()
    excel_path = data_dir / "Sample1.xls"
    pdf_path = data_dir / "Output-Chart_out.pdf"

    os.makedirs(data_dir, exist_ok=True)

    if not excel_path.is_file():
        ensure_sample_workbook(excel_path)

    workbook = cells.Workbook(str(excel_path))
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    chart.to_pdf(str(pdf_path))

    # Save chart to a memory stream
    ms = io.BytesIO()
    chart.to_pdf(ms)


if __name__ == "__main__":
    run()
