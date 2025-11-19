import io
import numpy as np
from sklearn.linear_model import LinearRegression
import aspose.cells as cells
from aspose.cells.charts import ChartType

# 1️⃣ Generate training data
# Assume sales are related to advertising spend
X = np.array([[10], [20], [30], [40], [50]])  # Advertising spend (ten thousand ¥)
y = np.array([25, 45, 65, 85, 105])           # Sales (ten thousand ¥)

# 2️⃣ Train a linear regression model using Scikit-learn
model = LinearRegression()
model.fit(X, y)

# 3️⃣ Predict new sales values
X_new = np.array([[60], [70], [80]])
y_pred = model.predict(X_new)

# 4️⃣ Create an Aspose.Cells workbook
wb = cells.Workbook()
ws = wb.worksheets[0]
ws.name = "Sales Prediction"

# Write headers
headers = ["Advertising (10k $)", "Actual Sales (10k $)", "Predicted Sales (10k $)"]
for i, h in enumerate(headers):
    cell = ws.cells.get(0, i)
    cell.put_value(h)
    style = cell.get_style()
    style.font.is_bold = True
    cell.set_style(style)

# Write training data
for r, (x, actual) in enumerate(zip(X.flatten(), y), start=1):
    ws.cells.get(r, 0).put_value(float(x))
    ws.cells.get(r, 1).put_value(float(actual))

# Write predicted data
start_row = len(y) + 2
for i, (x, pred) in enumerate(zip(X_new.flatten(), y_pred), start=start_row):
    ws.cells.get(i, 0).put_value(float(x))
    ws.cells.get(i, 2).put_value(float(pred))

# Auto-fit column widths
ws.auto_fit_columns()

# 5️⃣ Add a chart
charts = ws.charts
chart_idx = charts.add(ChartType.LINE, 10, 4, 30, 13)
chart = charts.get(chart_idx)
chart.title.text = "Sales Prediction"
# chart.n_series.add("B2:B6", True)
chart.n_series.add("C8:C10", True)
chart.n_series[0].name = "Predicted Sales"
# chart.n_series[1].name = "Predicted Sales"
chart.n_series.category_data = "A8:A10"

# 6️⃣ Save the result to an Excel file
wb.save("sales_prediction.xlsx", cells.SaveFormat.XLSX)
print("✅ Excel report saved as sales_prediction2.xlsx")
