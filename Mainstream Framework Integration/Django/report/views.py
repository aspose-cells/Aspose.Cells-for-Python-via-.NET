from django.shortcuts import render
from django.http import HttpResponse
import aspose.cells as cells
from aspose.cells.charts import ChartType
import io

# Homepage view
def index(request):
    return render(request, "index.html")


# Export Excel report
def export_report(request):
    # 1️⃣ Create a workbook
    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]
    sheet.name = "Sales Report"

    # 2️⃣ Write headers
    headers = ["Month", "Sales"]
    for i, h in enumerate(headers):
        cell = sheet.cells.get(0, i)
        cell.put_value(h)
        style = cell.get_style()
        style.font.is_bold = True
        cell.set_style(style)

    # 3️⃣ Write sample data
    data = [
        ("January", 12000),
        ("February", 18500),
        ("March", 15000),
        ("April", 21000),
        ("May", 19500),
    ]
    for r, (month, sales) in enumerate(data, start=1):
        sheet.cells.get(r, 0).put_value(month)
        sheet.cells.get(r, 1).put_value(sales)

    # 4️⃣ Auto-fit columns
    sheet.auto_fit_columns()

    # 5️⃣ Add a column chart
    charts = sheet.charts
    idx = charts.add(ChartType.COLUMN, 7, 4, 22, 10)
    chart = charts.get(idx)
    chart.title.text = "Monthly Sales"
    chart.n_series.add("B2:B6", True)
    chart.n_series.category_data = "A2:A6"

    # 6️⃣ Save to memory and return HttpResponse
    stream = io.BytesIO()
    workbook.save(stream, cells.SaveFormat.XLSX)
    stream.seek(0)

    response = HttpResponse(
        stream.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="sales_report.xlsx"'
    return response
