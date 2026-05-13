from pipeline.routing_pipeline import RoutingPipeline
from pipeline.execution_pipeline import ExecutionPipeline
from pipeline.report_pipeline import ReportPipeline


class ExcelAgent:

    def __init__(self):
        self.router = RoutingPipeline()
        self.executor = ExecutionPipeline()
        self.reporter = ReportPipeline()

    def run(self, file_path, output_file, user_request):

        print("Reading and planning...")

        plan = self.router.route(
            file_path=file_path,
            request=user_request
        )

        print(plan)

        results = self.executor.execute(
            file_path=file_path,
            plan=plan
        )

        self.reporter.generate(results,output_file)