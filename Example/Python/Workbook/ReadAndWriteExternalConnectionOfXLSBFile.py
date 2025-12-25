import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_read_and_write_external_connection_of_xlsb_file():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the source Excel Xlsb file
    input_path = os.path.join(source_dir, "sampleExternalConnection_XLSB.xlsb")
    workbook = cells.Workbook(input_path)

    # Read the first external connection which is a DB-Connection
    db_con = workbook.data_connections[0]
    if isinstance(db_con, cells.externalconnections.DBConnection):
        # Print the Name, Command and Connection Info of the DB-Connection
        print(f"Connection Name: {db_con.name}")
        print(f"Command: {db_con.command}")
        print(f"Connection Info: {db_con.connection_info}")

        # Modify the Connection Name
        db_con.name = "NewCust"

        # Save the Excel Xlsb file
        output_path = os.path.join(output_dir, "outputExternalConnection_XLSB.xlsb")
        workbook.save(output_path)

        print("ReadAndWriteExternalConnectionOfXLSBFile executed successfully.\n")
    else:
        print("The first data connection is not a DBConnection.")

if __name__ == "__main__":
    run_read_and_write_external_connection_of_xlsb_file()