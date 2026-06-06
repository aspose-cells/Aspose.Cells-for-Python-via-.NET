import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color
from pathlib import Path

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook"

def run():
    output_dir = get_output_directory()
    
    # Create empty workbook
    wb = Workbook()
    
    # Share the workbook
    wb.settings.shared = True
    
    # Update DaysPreservingHistory of RevisionLogs
    wb.worksheets.revision_logs.days_preserving_history = 7
    
    # Save the workbook
    output_path = os.path.join(output_dir, "outputShared_DaysPreservingHistory.xlsx")
    wb.save(output_path)

if __name__ == "__main__":
    run()