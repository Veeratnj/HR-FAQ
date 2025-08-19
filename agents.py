from textwrap import dedent

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.knowledge.json import JSONKnowledgeBase
from agno.vectordb.chroma import ChromaDb



model=Ollama(id="llama3.1:8b")

knowledge_base = JSONKnowledgeBase(
    json_files=["path/to/your/json/file.json"],
    vector_db=ChromaDb(collection="trigger1", path="knowledge-base", persistent_client=True)
    
)
knowledge_base.load(recreate=False)





trigger1 = Agent(
    name="trigger1",
    role="Analyze the patient report and find the fraudlent activities",
    model=model,
    tools=[],
    instructions=dedent("""\
    """),
    show_tool_calls=True,
    markdown=True,
)

trigger2 = Agent(
    name="trigger2",
    role="",
    model=model,
    tools=[],
    instructions=dedent("""\
        

    """),
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[trigger1,trigger2],
    model=model,
    instructions=dedent("""\
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)


if __name__=='__main__':

    agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA", stream=True
)













