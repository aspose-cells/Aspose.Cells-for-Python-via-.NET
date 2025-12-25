import os
import time
import threading
import aspose.cells as cells


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


class StopConversionOrLoadingUsingInterruptMonitor:
    def __init__(self):
        self.output_dir = get_output_directory()
        self.im = cells.InterruptMonitor()

    def create_workbook_and_convert_it_to_pdf_format(self):
        wb = cells.Workbook()
        wb.interrupt_monitor = self.im
        ws = wb.worksheets[0]
        cell = ws.cells.get("J1000000")
        cell.put_value("This is text.")
        try:
            wb.save(os.path.join(self.output_dir, "output_InterruptMonitor.pdf"))
        except cells.CellsException as ex:
            print("Process Interrupted - Message: " + ex.message)

    def wait_for_while_and_then_interrupt(self):
        time.sleep(10)
        self.im.interrupt()

    def test_run(self):
        t1 = threading.Thread(target=self.create_workbook_and_convert_it_to_pdf_format)
        t2 = threading.Thread(target=self.wait_for_while_and_then_interrupt)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    @staticmethod
    def run():
        StopConversionOrLoadingUsingInterruptMonitor().test_run()
        print("StopConversionOrLoadingUsingInterruptMonitor executed successfully.")


if __name__ == "__main__":
    StopConversionOrLoadingUsingInterruptMonitor.run()