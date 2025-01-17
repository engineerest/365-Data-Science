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

chat_template_time = ChatPromptTemplate.from_template('''
    I'm an intermediate level programmer.
    
    Consider the following literature:
    {books}
    
    Also, consider the following projects:
    {projects}
    
    Roughly how much time would it take me to complete the literature and the projects?
    
''')

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

chain_time1 = (RunnableParallel({'books': chain_books,
                                'projects': chain_projects})
              | chat_template_time
              | chat
              | string_parser
              )

chain_time2 = (({'books': chain_books,
                                'projects': chain_projects})
              | chat_template_time
              | chat
              | string_parser
              )

print(chain_time1.invoke({'programming language': 'Python'}))
print(chain_time2.invoke({'programming language': 'Python'}))

chain_parallel.get_graph().print_ascii()

