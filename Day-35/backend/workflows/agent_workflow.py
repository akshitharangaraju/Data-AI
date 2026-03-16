from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from tools.image_search import search_images


class AgentWorkflowService:

    def __init__(self):
        self.planner_agent = PlannerAgent()
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()

    def run(self, query: str):

        # Step 1 — Planning
        plan = self.planner_agent.plan(query)

        # Step 2 — Research
        research_data = self.research_agent.research(query)

        # Step 3 — Image Search
        images = search_images(query)

        # Step 4 — Final Answer
        result = self.writer_agent.write_answer(
            query=query,
            research_data=research_data,
            images=images
        )

        return result