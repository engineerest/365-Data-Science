from dotenv import load_dotenv

load_dotenv('.env')

from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

chat_template = ChatPromptTemplate.from_messages([
    ('human',
     '''I've recently adopted a {pet} which is a {breed}. Could you suggest several training tips?''')
])

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

chain = chat_template | chat

print(type(chain))

# Runnable class:
# Prompt Template
# Chat Model
# Output Parser

print(type(chat_template))

# The implementation of ChatPromptTemplate starts
# with the Runnable class, therefore inhereting the invoke(),
# batch(), and stream() methods.

