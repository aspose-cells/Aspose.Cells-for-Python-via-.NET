from excel.writer import ExcelWriter


class ReportPipeline:

    def generate(self, results,output_path):

        ExcelWriter.write_report(
            output_path=output_path,
            reports=results
        )

        print("Report generated.")