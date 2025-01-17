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

# invoke()
# The invoke() method doesn't allow for feeding several input at once.
# chain.invoke({'pet': '...', 'breed': '...'})
# chain.invoke({'pet': '...', 'breed': '...d'})

# batch()
# The batch() method runs invoke() in parallel.
# The process is less time-consuming than running
# several subsequent invoke() methods.

# %%time
print(chain.batch([{'pet': 'dog', 'breed': 'shepherd'},
                   {'pet': 'dragon', 'breed' : 'night fury'}]))
# %%time
print(chain.invoke({'pet': 'dog', 'breed': 'shepherd'}))
# %%time
print(chain.invoke({'pet': 'dragon', 'breed' : 'night fury'}))

# We anticipate:
# Ex. time of batch() < Ex. time of invoke() + Ex. time of invoke()

# Passing several inputs at once of a batch()
# method is much more time-efficient than
# invoking the chain that many times in sequence

# This can scale up significantly with more dictionaries and lengthier responses