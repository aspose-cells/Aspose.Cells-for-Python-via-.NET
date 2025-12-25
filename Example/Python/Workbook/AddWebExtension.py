import os
import aspose.cells as cells
from aspose.cells.webextensions import WebExtensionStoreType

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_add_web_extension():
    out_dir = get_output_directory()

    workbook = cells.Workbook()

    extensions = workbook.worksheets.web_extensions
    task_panes = workbook.worksheets.web_extension_task_panes

    extension_index = extensions.add()
    task_pane_index = task_panes.add()

    extension = extensions[extension_index]
    extension.reference.id = "wa104379955"
    extension.reference.store_name = "en-US"
    extension.reference.store_type = WebExtensionStoreType.OMEX

    task_pane = task_panes[task_pane_index]
    task_pane.is_visible = True
    task_pane.dock_state = "right"
    task_pane.web_extension = extension

    output_path = os.path.join(out_dir, "AddWebExtension_Out.xlsx")
    workbook.save(output_path)

    print("AddWebExtension executed successfully.")

if __name__ == "__main__":
    run_add_web_extension()