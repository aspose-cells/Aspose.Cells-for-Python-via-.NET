import tensorflow as tf
import numpy as np
import aspose.cells as cells

# -----------------------------
# Step 1: Prepare training data
# -----------------------------
# y = 2x + 1
x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
y_train = 2 * x_train + 1
print(y_train)
# -----------------------------
# Step 2: Define and train the model
# -----------------------------
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x_train, y_train, epochs=200, verbose=0)

# -----------------------------
# Step 3: Predict with the trained model
# -----------------------------
x_test = np.arange(10, 20, 1, dtype=float)   # New data
y_pred = model.predict(x_test).flatten()     # Predicted values

print("Predicted values:", y_pred)

# -----------------------------
# Step 4: Write prediction results to Excel
# -----------------------------
wb = cells.Workbook()
sheet = wb.worksheets[0]

# Write headers
sheet.cells.get(0, 0).put_value("X")
sheet.cells.get(0, 1).put_value("Predicted Y")

# Write data
for i, (x_val, y_val) in enumerate(zip(x_test, y_pred)):
    sheet.cells.get(i + 1, 0).put_value(float(x_val))
    sheet.cells.get(i + 1, 1).put_value(float(y_val))

# -----------------------------
# Step 5: Create a chart
# -----------------------------
chart_index = sheet.charts.add(cells.charts.ChartType.LINE, 5, 5, 20, 15)
chart = sheet.charts[chart_index]
chart.n_series.add("B2:B11", True)
chart.n_series.category_data = "A2:A11"
chart.title.text = "Predicted y = 2x + 1"
chart.n_series[0].name = "Predicted Y"
chart.n_series[0].data_labels.show_value = True
# -----------------------------
# Step 6: Save Excel file
# -----------------------------
wb.save("tensorflow_prediction.xlsx")
print("Excel file generated: tensorflow_prediction.xlsx")

