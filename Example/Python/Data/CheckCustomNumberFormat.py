import aspose.cells as cells

def run_check_custom_number_format():
    wb = cells.Workbook()
    wb.settings.check_custom_number_format = True

    ws = wb.worksheets[0]
    c = ws.cells.get("A1")
    c.put_value(2347)

    s = c.get_style()
    try:
        s.custom = "ggg @ fff"  # Invalid custom number format
        c.set_style(s)
    except Exception as ex:
        print("Exception Occurred. Exception:", ex)

    print("CheckCustomNumberFormat executed successfully.")


if __name__ == "__main__":
    run_check_custom_number_format()