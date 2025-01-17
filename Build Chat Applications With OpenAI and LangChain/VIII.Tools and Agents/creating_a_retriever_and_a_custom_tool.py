from dotenv import load_dotenv

load_dotenv('.env')

from langchain_community.vectorstores import Chroma

from langchain.embeddings import OpenAIEmbeddings

from langchain_core.tools import tool
from langchain.agents import create_retriever_tool

from platform import python_version

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

print(retriever_tool)

print(retriever_tool.args)

print(retriever_tool.invoke("Could you list the programming languages a data scientist should know?"))

@tool
def get_python_version() -> str:
    '''Useful for questions regarding the version of Python currently used.'''
    return python_version()

print(get_python_version)

@tool("Another Name")
def get_python_version() -> str:
    '''Useful for questions regarding the version of Python currently used.'''
    return python_version()

print(get_python_version)

print(get_python_version.args)

print(get_python_version.invoke({}))
