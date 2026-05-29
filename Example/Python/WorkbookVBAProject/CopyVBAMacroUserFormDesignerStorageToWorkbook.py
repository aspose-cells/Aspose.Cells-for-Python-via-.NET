import os
from aspose.cells import Workbook, SaveFormat
from aspose.cells.vba import VbaModuleType

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    target = Workbook()
    
    template_file = Workbook(os.path.join(source_dir, "sampleDesignerForm.xlsm"))
    
    for worksheet in template_file.worksheets:
        if worksheet.type == "WORKSHEET":
            s = target.worksheets.add(worksheet.name)
            s.copy(worksheet)
            s.cells.get("A2").put_value("VBA Macro and User Form copied from template to target.")
    
    # Handle ThisWorkbook module separately
    for vba_item in template_file.vba_project.modules:
        if vba_item.name == "ThisWorkbook":
            # Find the ThisWorkbook module in target (it should be created automatically)
            for target_module in target.vba_project.modules:
                if target_module.name == "ThisWorkbook":
                    target_module.codes = vba_item.codes
                    break
    
    # Handle other modules
    for vba_item in template_file.vba_project.modules:
        if vba_item.name != "ThisWorkbook":
            sheet = target.worksheets.get_sheet_by_code_name(vba_item.name)
            if sheet is None:
                vba_mod_index = target.vba_project.modules.add(vba_item.type, vba_item.name)
            else:
                vba_mod_index = target.vba_project.modules.add(sheet)
            
            # Get the module by index
            target_module = target.vba_project.modules[vba_mod_index]
            target_module.codes = vba_item.codes
            
            if vba_item.type == VbaModuleType.DESIGNER:
                designer_storage = template_file.vba_project.modules.get_designer_storage(vba_item.name)
                target.vba_project.modules.add_designer_storage(vba_item.name, designer_storage)
    
    target.save(os.path.join(output_dir, "outputDesignerForm.xlsm"), SaveFormat.XLSM)

if __name__ == "__main__":
    run()