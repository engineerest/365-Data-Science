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

# question = "Can you give me an interesting fact I probably didn't know about?"
question = "Can you elaborate a bit more on this fact?"

dictionary_output = RunnablePassthrough.assign(
    message_log=RunnableLambda(chat_memory.load_memory_variables) |
    itemgetter('message_log')).invoke(
    {'question': question})

print(prompt_template.invoke(dictionary_output))

prompt_value_output = prompt_template.invoke(dictionary_output)

print(chat.invoke(prompt_value_output))

ai_message_output = chat.invoke(prompt_value_output)

print(StrOutputParser.invoke(ai_message_output))

response = StrOutputParser.invoke(ai_message_output)

chat_memory.save_context(inputs={'input': question},
                         outputs={'output': response})

chain1 = (
    RunnablePassthrough.assign(
        message_log=RunnableLambda(chat_memory.load_memory_variables) |
        itemgetter('message_log'))
    | prompt_template
    | chat
    | StrOutputParser()
)

question = "Can you give me an interesting fact I probably didn't know about?"

response = chain1.invoke({'question': question})

chat_memory.save_context(inputs={'input': question},
                         outputs={'output': response})

print(response)

@chain
def memory_chain(question):
    chain1 = (
        RunnablePassthrough.assign(
            message_log=RunnableLambda(chat_memory.load_memory_variables) |
            itemgetter('message_log'))
        | prompt_template
        | chat
        | StrOutputParser()
    )

    response = chain1.invoke({'question': question})

    chat_memory.save_context(inputs={'input': question},
                             outputs={'output': response})

    return response

print(memory_chain.invoke({'question': "Can you give me an interesting fact I probably didn't know about?"}))