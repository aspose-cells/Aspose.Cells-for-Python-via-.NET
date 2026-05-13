from llm.planner import Planner


class RoutingPipeline:

    def __init__(self):
        self.planner = Planner()

    def route(self, file_path, request):
        return self.planner.create_plan(request)