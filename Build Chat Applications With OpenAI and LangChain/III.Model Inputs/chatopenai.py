from dotenv import load_dotenv
load_dotenv('.env')
# Sufficient for LangChain to locate the required environment variable

from langchain.chat_models import ChatOpenAI

# chat = ChatOpenAI(model_name='gpt-4', seed=365)
# WARNING! seed is not default parameter.
#                     seed was transferred to model_kwargs.
#                     Please confirm that seed is what you intended.

# chat = ChatOpenAI(model_name='gpt-4', model_kwargs={'seed': 365})
# You can add other parameters by specifying them as key-value pairs within the same dictionary

chat = ChatOpenAI(model_name='gpt-4o-mini', model_kwargs={'seed': 365}, temperature=0, max_tokens=100)
# Controls the level of randomness in responses

response = chat.invoke(''' I've recently adopted a dog. Could you suggest some dog names? ''')
# LangChain Expression Language (LCEL)

# Accepts various inputs, including a string-type object,
# containing the user prompt.

print(response)

print(response.content)

