from dotenv import load_dotenv

load_dotenv('.env')

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.chat_models import ChatOpenAI

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia_api = WikipediaAPIWrapper()
# Fetch articles through the loa() method.
# Fetch page summaries through the run() method.

print(wikipedia_api.run('Python'))
# We'll resolve this warning in the text lesson that follows

wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api)

print(wikipedia_tool.name)
print(wikipedia_tool.description)
print(wikipedia_tool.args)

response = wikipedia_tool.invoke({'query': 'Python'})

print(response)

print(wikipedia_tool.invoke('Python'))

TEMPLATE = '''
Turn the following user input into a Wikipedia search query. Don't answer the question:

{input}
'''

prompt_template = PromptTemplate.from_template(TEMPLATE)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0
)

chain = prompt_template | chat | StrOutputParser()

print(chain.invoke({'input': 'Who is the creator of the Python programming language?'}))
