from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain_core.prompts.chat import (SystemMessagePromptTemplate,
                                         HumanMessagePromptTemplate,
                                         ChatPromptTemplate)

chat = ChatOpenAI(model_name='gpt-4',
                  model_kwargs={'seed': 365},
                  temperature=0,
                  max_tokens=100)

TEMPLATE_S = '{description}'
TEMPLATE_H = '''I've recently adopted a {pet}. Could you suggest some {pet} names?'''

message_template_s = SystemMessagePromptTemplate.from_template(template=TEMPLATE_S)
print(message_template_s)

message_template_h = HumanMessagePromptTemplate.from_template(template=TEMPLATE_H)
print(message_template_h)

chat_template = ChatPromptTemplate.from_messages([message_template_s, message_template_h])

print(chat_template)

chat_value = chat_template.invoke({'description': '''The chatbot should reluctantly answer questions 
with sarcastic responses.''', 'pet':'''dog'''})

print(chat_value)

response = chat.invoke(chat_value)
# ChatOpenAI's invoke()
# String
# List of chat messages
# PromptValue

print(response)

# invoke()
# Class                 Accepts                 Returns
# ChatPromptTemplate    Dictionary              ChatPromptValue
# ChatOpenAI            ChatPromptValue         AIMessage

# The stepping stone toward understanding how chains in LangChain work.