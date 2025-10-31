from flask import Flask, send_file, render_template
import io
import aspose.cells as cells
from aspose.cells.charts import ChartType

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download-report")
def download_report():
    # Create a workbook
    wb = cells.Workbook()
    ws = wb.worksheets[0]
    ws.name = "Sales Report"

    # Write header row
    headers = ["Product", "Region", "Month", "Sales", "Profit"]
    for i, h in enumerate(headers):
        ws.cells.get(0, i).value = h
    header_range = ws.cells.create_range("A1:E1")
    header_range.set_style(make_bold(wb))

    # Write sample data
    data = [
        ["Laptop", "Europe", "Jan", 1200, 300],
        ["Tablet", "Asia", "Feb", 900, 250],
        ["Phone", "US", "Mar", 1500, 500],
        ["Headphones", "Europe", "Apr", 700, 150],
        ["Camera", "Asia", "May", 1100, 400],
    ]
    for r, row in enumerate(data, start=1):
        for c, v in enumerate(row):
            ws.cells.get(r, c).value = v

    # Create a column chart
    charts = ws.charts
    chart_index = charts.add(ChartType.COLUMN, 7, 4, 22, 10)  # Add column chart at specified location
    chart = charts[chart_index]
    chart.title.text = "Sales vs Profit"
    chart.n_series.add("D2:E6", True)  # Add series for Sales and Profit
    chart.n_series.category_data = "A2:A6"  # Set categories from Product column

    # Output the workbook to an in-memory file
    stream = io.BytesIO()
    wb.save(stream, cells.SaveFormat.XLSX)
    stream.seek(0)

    return send_file(
        stream,
        as_attachment=True,
        download_name="sales_report.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


def make_bold(wb):
    style = wb.create_style()
    font = style.font
    font.is_bold = True
    return style


if __name__ == "__main__":
    app.run(debug=True)
