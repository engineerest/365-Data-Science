from dotenv import load_dotenv

load_dotenv('.env')

from langchain_community.vectorstores import Chroma

from langchain.embeddings import OpenAIEmbeddings

from langchain_core.tools import tool
from langchain.agents import create_retriever_tool

from langchain.chat_models import ChatOpenAI

from langchain_community.utilities import WikipediaQueryRun
from langchain_community.tools import WikipediaAPIWrapper

from langchain.agents import create_tool_calling_agent, AgentExecutor

from langchain import hub

from platform import python_version

wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

vectorstore = Chroma(
    persist_directory='./intro-to-ds-lectures',
    embedding_function=OpenAIEmbeddings()
)

retriever = vectorstore.as_retriever(
    search_type='mmr',
    search_kwargs={
        'k': 3,
        'lambda_mult': 0.7
    }
)

retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="Introduction-to-Data-and-Data-Science-Course-Lectures",
    description='''
    For any questions regarding the Introduction to Data and Data Science course.
    you must use this tool.
    '''
)

@tool
def get_python_version() -> str:
    '''Useful for questions regarding the version of Python currently used.'''
    return python_version()

tools = [wikipedia_tool, retriever_tool, get_python_version]

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0
)

chat_prompt_template = hub.pull("hwchase17/openai-tools-agent")

agent = create_retriever_tool(
    llm=chat,
    tools=tools,
    prompt=chat_prompt_template
)
# We need to create an agent executor to carry out the agent's decisions

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True
)

print(agent_executor.invoke({'input', "Could you tell me the version of Python I'm currently using?"}))

response = agent_executor.invoke({'input', "Could you tell me the version of Python I'm currently using?"})
print(response)

response = agent_executor.invoke({'input':
                                  '''I'm currently following the Introduction to Data and Data Science course.
                                  Could you lst the programming languages a data scientist should know?
                                  Additionally, cold you tell me who their creators are?'''})

print(response)