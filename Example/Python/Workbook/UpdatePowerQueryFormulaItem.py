import os
import aspose.cells as cells


def get_source_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "Data", "01_SourceDirectory")
    )


def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "Data", "02_OutputDirectory")
    )


def run_update_power_query_formula_item():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "SamplePowerQueryFormula.xlsx")
    workbook = cells.Workbook(input_path)

    mashup_data = workbook.data_mashup
    for formula in mashup_data.power_query_formulas:
        for item in formula.power_query_formula_items:
            if item.name == "Source":
                item.value = f'Excel.Workbook(File.Contents("{os.path.join(source_dir, "SamplePowerQueryFormulaSource.xlsx")}"), null, true)'

    output_path = os.path.join(output_dir, "SamplePowerQueryFormula_out.xlsx")
    workbook.save(output_path)

    print("UpdatePowerQueryFormulaItem executed successfully.")


if __name__ == "__main__":
    run_update_power_query_formula_item()