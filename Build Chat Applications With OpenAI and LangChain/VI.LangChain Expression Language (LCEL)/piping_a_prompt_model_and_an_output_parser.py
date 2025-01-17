from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

list_instructions = CommaSeparatedListOutputParser().get_format_instructions()
print(list_instructions)

chat_template = ChatPromptTemplate.from_messages([
    ('human', "I've recently adopted a {pet}. Could you suggest some {pet} names? \n" + list_instructions),
])
print(chat_template)

# We didn't need to import and create an instance of this class. It was done for us

print(chat_template.messages[0].prompt.template)

chat = ChatOpenAI(model_name='gpt-4',
                  model_kwargs={'seed': 365},
                    temperature=0,
                    max_tokens=100)

list_output_parser = CommaSeparatedListOutputParser()
print(chat_template.invoke({'pet': 'dog'})) # Stores the filled in HumanMessagePromptTemplate as a HumanMessage object.

chat_template_result = chat_template.invoke({'pet': 'dog'})
print(chat_template_result)

chat_result = chat.invoke(chat_template_result)

print(list_output_parser.invoke(chat_result))

chain = chat_template | chat | list_output_parser
# Pipe Symbol: Links elements in the expression language,
# showing the output will be the input for the text component

print(chat.invoke({'pet': 'dog'}))

