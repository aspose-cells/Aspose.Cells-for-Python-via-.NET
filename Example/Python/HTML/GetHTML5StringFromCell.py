import aspose.cells as cells

def run_get_html5_string_from_cell():
    # Create workbook.
    workbook = cells.Workbook()
    
    # Access first worksheet.
    worksheet = workbook.worksheets[0]
    
    # Access cell A1 and put some text inside it.
    cell = worksheet.cells.get("A1")
    cell.put_value("This is some text.")
    
    # Get the Normal and Html5 strings.
    str_normal = cell.get_html_string(False)
    str_html5 = cell.get_html_string(True)
    
    # Print the Normal and Html5 strings on console.
    print("Normal:\r\n" + str_normal)
    print()
    print("Html5:\r\n" + str_html5)
    
    print("GetHTML5StringFromCell executed successfully.")

if __name__ == "__main__":
    run_get_html5_string_from_cell()