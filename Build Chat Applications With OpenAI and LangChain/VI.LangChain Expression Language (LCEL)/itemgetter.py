from dotenv import load_dotenv

load_dotenv('.env')

from langchain.memory import ConversationSummaryMemory
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from operator import itemgetter

TEMPLATE = '''
The following is a friendly conversation between a human and an AI.
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{message_log}

Human:
{question}

AI:
'''

prompt_template = PromptTemplate.from_template(template=TEMPLATE)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

chain = prompt_template | chat | StrOutputParser()

print(chain.invoke({'message_log': '',
              'question': "Can you give me an interesting fact I probably didn't know about?"}))

print(chain.invoke({'message_log': '''The AI provides an interesting fact about octopuses, stating that they hae three hearts.
                Two hearts pump blood to the gills, while the third heart pumps it to the rest of the body.''',
              'question': "Can you elaborate a bit more on this fact?"}))

chat_memory = ConversationSummaryMemory(llm=ChatOpenAI(),
                                        memory_key='message_log')

print(chat_memory.load_memory_variables({}))

print(RunnablePassthrough().invoke('hi!'))

print(RunnablePassthrough().invoke({'question': "Can you give me an interesting fact I probably didn't know about?"}))

print(RunnablePassthrough().invoke({'input': 'hi'}))

print(RunnablePassthrough.assign(first_letter=lambda x: list(x['input'])[0],
                                 second_letter=lambda x: list(x['input'])[1]).invoke({'input': 'hi'}))

print([0, 1, 2, 3].__getitem__(1))

print((0, 1, 2, 3).__getitem__(1))

print('hi'.__getitem__(1))

print({'key': 'value'}.__getitem__('key'))

print(itemgetter(0)('hi'))

print(itemgetter(0)([0, 1, 2, 3]))

print(itemgetter('message')({'message_log': ''}))

print(RunnableLambda(itemgetter('message_log')).invoke({'message_log': ''}))

print(RunnablePassthrough().invoke(message_log=
                                   RunnableLambda(chat_memory.load_memory_variables) |
                                   RunnableLambda(itemgetter('message_log'))
                                   ).invoke({'question': "Can you give me an interesting fact I probably didn't know about?"}))

