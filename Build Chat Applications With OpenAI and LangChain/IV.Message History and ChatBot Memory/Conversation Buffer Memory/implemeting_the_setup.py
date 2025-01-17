from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain_core.messages import SystemMessage
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    MessagesPlaceholder)

from langchain.chains.llm import LLMChain

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory

from langchain.globals import set_verbose
# Displays the output in a verbose mode.
# We'll see the chatbot's final response and
# the intermediate steps.
# Allows for better monitoring of the process
# and helps with debugging
set_verbose(True)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

message_s = SystemMessage(content='''The chatbot should rely on the conversation history to answer questions with sarcastic responses.''')
message_template_h = HumanMessagePromptTemplate.from_template(template='''{question}''')

# Task: Create a placeholder for all intermediate messages we log - MessagesPlaceholder

message_history = MessagesPlaceholder(variable_name='message_log') # Feel free to use any text you prefer

chat_template = ChatPromptTemplate.from_messages([message_s, message_history, message_template_h])
print(chat_template)

# ChatMessageHistory instances are convenient for feeding context into a memory object.

background_info = ChatMessageHistory()
background_info.add_user_message('Hi!')
background_info.add_ai_message("You really know how to make an entrance, don't you?")

# It's time to create the memory object

# Configuring the Chain

#
# chat_memory = ConversationBufferMemory(memory_key='message_log',
#                                        chat_memory=background_info,
#                                        return_messages=False)

# Change on ConversationBufferWindowMemory

chat_memory = ConversationBufferWindowMemory(memory_key='message_log',
                                             chat_memory=background_info,
                                             return_messages=False,
                                             k=2) # Effect of earlier conversation
# True
# The memory is returned as a list of chat messages.

# False
# The memory is returned as a string.

print(chat_memory.load_memory_variables({}))

print(chat_memory.load_memory_variables({})['message_log'])

chat_memory = ConversationBufferMemory(memory_key='message_log',
                                       chat_memory=background_info,
                                       return_messages=True)

print(chat_memory.load_memory_variables({}))

print(chat_memory.load_memory_variables({})['message_log'])


chain = LLMChain(
    llm=chat,
    prompt=chat_template,
    memory=chat_memory
)
# Set new line
set_verbose(False)

# response = chain.invoke({'question': "Can you give me an interesting fact I probably didn't know about?"})
# response = chain.invoke({'question': "Can you elaborate a bit more on this fact?"})
# response = chain.invoke({'question': "What are other interesting collective nouns?"})
response = chain.invoke({'question': "Can you tell me something interesting about alligators?"})
print(response)

print(response['text'])

# str_verbose(True)

# Sets the verbose parameter of each class to True, where present.

print(chat.verbose, chain.verbose)

# As the conversation grows:
# x the chatmodel needs more time to respond.
# x uses up more and more prompt tokens.

# How to Remedy These Issues
# v Enforcing a cap on the number of interactions.
# v The earliest messages are dropped from the memory.

print(response['text']

      )