from crewai import Task
from agent import calculator_agent

calculator_task = Task(
    description = "Calculate 2+2. ",
    expected_output = "Return only the numerical answer.",
    agent = calculator_agent

)