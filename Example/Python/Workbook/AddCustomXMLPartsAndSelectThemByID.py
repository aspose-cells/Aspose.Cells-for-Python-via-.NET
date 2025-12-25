import aspose.cells as cells

def main():
    # Create empty workbook.
    wb = cells.Workbook()

    # Some data in the form of byte array.
    # Please use correct XML and Schema instead.
    bts_data = bytes([1, 2, 3])
    bts_schema = bytes([1, 2, 3])

    # Create four custom xml parts.
    wb.custom_xml_parts.add(bts_data, bts_schema)
    wb.custom_xml_parts.add(bts_data, bts_schema)
    wb.custom_xml_parts.add(bts_data, bts_schema)
    wb.custom_xml_parts.add(bts_data, bts_schema)

    # Assign ids to custom xml parts.
    wb.custom_xml_parts[0].id = "Fruit"
    wb.custom_xml_parts[1].id = "Color"
    wb.custom_xml_parts[2].id = "Sport"
    wb.custom_xml_parts[3].id = "Shape"

    # Specify search custom xml part id.
    srch_id = "Fruit"
    srch_id = "Color"
    srch_id = "Sport"

    # Search custom xml part by the search id.
    cxp = wb.custom_xml_parts.select_by_id(srch_id)

    # Print the found or not found message on console.
    if cxp is None:
        print(f"Not Found: CustomXmlPart ID {srch_id}")
    else:
        print(f"Found: CustomXmlPart ID {srch_id}")

    print("AddCustomXMLPartsAndSelectThemByID executed successfully.")


if __name__ == "__main__":
    main()