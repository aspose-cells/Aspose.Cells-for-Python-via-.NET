import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_access_web_extension_information():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "WebExtensionsSample.xlsx")
    workbook = cells.Workbook(workbook_path)

    task_panes = workbook.worksheets.web_extension_task_panes

    for task_pane in task_panes:
        print(f"Width: {task_pane.width}")
        print(f"IsVisible: {task_pane.is_visible}")
        print(f"IsLocked: {task_pane.is_locked}")
        print(f"DockState: {task_pane.dock_state}")
        print(f"StoreName: {task_pane.web_extension.reference.store_name}")
        print(f"StoreType: {task_pane.web_extension.reference.store_type}")
        print(f"WebExtension.Id: {task_pane.web_extension.id}")

    print("AccessWebExtensionInformation executed successfully.")

if __name__ == "__main__":
    run_access_web_extension_information()
