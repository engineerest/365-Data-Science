from dotenv import load_dotenv

load_dotenv('.env')

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough # Passes inputs through without alteration.
# LangChain's identify function

print(RunnablePassthrough().invoke('hi'))
print(RunnablePassthrough().invoke([1, 2, 3]))

# Main Task:
# Combine two chains where:
# 1. The first chain lists the most essential tools for a given profession.
# 2. The second chain suggests strategies for mastering the tools provided in the first chain.

chat_template_tools = ChatPromptTemplate.from_messages(
    '''What are the five most important tools a {job title} needs?
    Answer only by listing the tools.'''
) # {job title} - A placeholder for a profession the user enters.

chat_template_strategy = ChatPromptTemplate.from_template(
    '''Considering the tools provided, develop a strategy for effectively learning and mastering them:
    {tools}'''
)

# Display the prompt template for the first chain (optional, for debugging purposes).
# print(chat_template_tools)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

string_parser = StrOutputParser()

chain_tools = chat_template_tools | chat | string_parser | {'tools': RunnablePassthrough}
chain_strategy = chat_template_strategy | chat | string_parser

# Execute the first chain to list essential tools for a profession.
tools_output = chain_tools.invoke({'job title': 'data scientist'})
print(tools_output)

# Execute the second chain to generate strategies for mastering the tools.
strategy_output = chain_strategy.invoke({
    'tools': '''
                1. Python
                2. R Programming
                3. SQL
                4. Tableau
                5. Hadoop'''
})
print(strategy_output)

#                                                                                                          1. Python
#                                                                                                          2. R Programming
#                                                                                                          3. SQL
#                                                                                                          4. Tableau
#                                                          ChatPromptValue      AIMessage                  5. Hadoop
# {'job title; : 'data scientist'} -> chat_template_tools ---------------> chat ---------> string_parser --------------------> RunnablePassthrough ---> tools:1. Python
#                                                                                                                                                           2. R Programming
#                                                                                                                                                           3. SQL
#                                                                                                                                                           4. Tableau
#                                                                                                                                                           5. Hadoop

# Invoking chain_strategy with the output of chain_tools will connect the two runnables

chain_combined = chain_tools | chain_strategy
print(chain_combined.invoke({'job title': 'data scientist'}))

chain_long = (chat_template_tools | chat | string_parser | {'tools': RunnablePassthrough} |
              chat_template_strategy | chat | string_parser)

