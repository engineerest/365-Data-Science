from dotenv import load_dotenv

load_dotenv('.env')

from langchain.prompts import ChatPromptTemplate
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

print(chain.invoke({'pet': 'dog', 'breed': 'shepherd'}))

# %%time
print(chain.batch([{'pet': 'dog', 'breed': 'shepherd'},
                   {'pet': 'dragon', 'breed' : 'night fury'}]))
# %%time
print(chain.invoke({'pet': 'dog', 'breed': 'shepherd'}))
# %%time
print(chain.invoke({'pet': 'dragon', 'breed' : 'night fury'}))

# stream()

print(chain.stream({'pet': 'dog', 'breed': 'shepherd'}))

response = chain.stream({'pet': 'dragon', 'breed' : 'night fury'})
print(next(response))

# StopIteration:
# The response generator has exhausted all its elements; it can no longer be used

for i in response:
    print(i.content, end='')

# LangChain Expression Language
# Piped components to form chains.
# Applied the invoke(), batch(), and stream() methods.
# Discuss the nature of the LCEL chains.
# Explore the type of objects they represent.