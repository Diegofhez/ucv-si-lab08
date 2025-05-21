from fontTools.ttLib.tables.ttProgram import instructions
from google.adk.agents import LlmAgent
from google.adk.tools import google_search


dict_agent = LlmAgent(
    model="gemini-2.0- flash-exp",
    name= "Diego_agent",
    description="Este agente sirve para darte la hora",
    instruction= """Respond to the query using google search""",
    tools=[google_search],
)
