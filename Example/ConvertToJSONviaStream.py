import io
from aspose.cells import Workbook, SaveFormat

# Read the input file into a memory stream
with open('HelloWorld.xlsx', 'rb') as file:
    input_stream = io.BytesIO(file.read())

# Create a Workbook object
workbook = Workbook(input_stream)

# Save to a memory stream
out_stream = io.BytesIO()
workbook.save(out_stream, SaveFormat.JSON)

# Write the memory stream to an output file
with open('HelloWorld.json', 'wb') as f:
    f.write(out_stream.getvalue())
