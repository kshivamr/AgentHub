from crewai import Crew
from task import calculator_task

crew = Crew(
    agents = [calculator_task.agent],
    tasks = [calculator_task],
    verbose = True
)

result = crew.kickoff()

print(result.raw)
