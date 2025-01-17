from dotenv import load_dotenv

load_dotenv('.env')

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


print(RunnablePassthrough().invoke('hi'))
print(RunnablePassthrough().invoke([1, 2, 3]))

chat_template_tools = ChatPromptTemplate.from_messages(
    '''What are the five most important tools a {job title} needs?
    Answer only by listing the tools.'''
)

chat_template_strategy = ChatPromptTemplate.from_template(
    '''Considering the tools provided, develop a strategy for effectively learning and mastering them:
    {tools}'''
)


chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

string_parser = StrOutputParser()

chain_tools = chat_template_tools | chat | string_parser | {'tools': RunnablePassthrough}
chain_strategy = chat_template_strategy | chat | string_parser

tools_output = chain_tools.invoke({'job title': 'data scientist'})
print(tools_output)

strategy_output = chain_strategy.invoke({
    'tools': '''
                1. Python
                2. R Programming
                3. SQL
                4. Tableau
                5. Hadoop'''
})
print(strategy_output)

chain_combined = chain_tools | chain_strategy
print(chain_combined.invoke({'job title': 'data scientist'}))

chain_long = (chat_template_tools | chat | string_parser | {'tools': RunnablePassthrough} |
              chat_template_strategy | chat | string_parser)

chain_long.get_graph().print_ascii()
# A straighforward chain to visualize

# Graphs can branch when addressing parallel precesses.
