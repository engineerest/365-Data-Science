from dotenv import load_dotenv

load_dotenv('.env')

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

chat_template_books = ChatPromptTemplate.from_template(
    '''
    Suggest three of the best intermediate-level {programming language} books.
    Answer only by listing the books.
    '''
)

chat_template_projects = ChatPromptTemplate.from_template(
    '''
    Suggest three interesting {programming language} projecys suitable for intermediate-level programmers.
    Answer only  by listing the projects.
    '''
)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

string_parser = StrOutputParser

chain_books = chat_template_books | chat | string_parser

chain_projects = chat_template_projects | chat | string_parser

chain_parallel = RunnableParallel(
    {'books': chain_books, 'projects': chain_projects}
)

print(chain_parallel.invoke({'programming language': 'Python'}))

chain_parallel.get_graph().print_ascii()

# batch()
# Allowed us to invoke the same Runnable with
# different input values.

# RunnableParallel
# Allows us to execute several using identical
# input values

# %%time
print(chain_books.invoke({'programming language': 'Python'}))

# %%time
print(chain_projects.invoke({'programming language': 'Python'}))

# %%time
print(chain_parallel.invoke({'programming language': 'Python'}))

