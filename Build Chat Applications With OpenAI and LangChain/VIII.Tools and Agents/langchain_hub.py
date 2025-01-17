from dotenv import load_dotenv

load_dotenv('.env')

from langchain_community.vectorstores import Chroma

from langchain.embeddings import OpenAIEmbeddings

from langchain_core.tools import tool
from langchain.agents import create_retriever_tool

from langchain.chat_models import ChatOpenAI

from langchain_community.utilities import WikipediaQueryRun
from langchain_community.tools import WikipediaAPIWrapper

from langchain.prompts import (
    PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder,
    ChatPromptTemplate,
                               )

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
    name="Introduction to Data and Data Science Course Lectures",
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
print(chat_prompt_template)

print(chat_prompt_template.pretty_print())

print(ChatPromptTemplate(input_variables=['agent_scratchpad', 'input'],
                    input_types={'chat_history': typing.List[typing.Union[langchain_core.messages.ai.AIMessage,
                                                                            langchain_core.messages.human.HumanMessage,
                                                                            langchain_core.messages.chat.ChatMessage,
                                                                            langchain_core.messages.system.SystemMessage,
                                                                            langchain_core.messages.function.FunctionMessage,
                                                                            langchain_core.messages.tool.ToolMessage]],
                                'agent_scratchpad': typing.List[typing.Union [langchain_core.messages.ai.AIMessage,
                                                                            langchain_core.messages.human.HumanMessage,
                                                                            langchain_core.messages.chat.ChatMessage,
                                                                            langchain_core.messages.system. SystemMessage,
                                                                            langchain_core.messages.function.FunctionMessage,
                                                                            langchain_core.messages.tool.ToolMessage]]},
                    messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables =[],
                                                                                template='You are are a helpful assistant')),
                                MessagesPlaceholder(variable_name='chat_history', optional=True),
                                HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'],
                                                                                template='{input}')),
                                MessagesPlaceholder(variable_name='agent_scratchpad')]))