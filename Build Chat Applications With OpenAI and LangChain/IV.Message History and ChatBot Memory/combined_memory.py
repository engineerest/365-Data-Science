from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import (ConversationBufferMemory,
                              ConversationSummaryMemory,
                              CombinedMemory)

TEMPLATE = '''
The following is a friendly conversation between a human and an AI.
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Past messages:
{message_buffer_log}

Conversation summary:
{message_summary_log}

Human: {question}
AI:
'''

prompt_template = PromptTemplate.from_template(TEMPLATE)

chat_buffer_memory = ConversationBufferMemory(memory_key='message_buffer_log',
                                              return_messages=False)

chat_summary_memory = ConversationSummaryMemory(llm=ChatOpenAI(),
                                                memory_key='message_summary_log',
                                                input_key='question',
                                                return_messages=False)

chat_combined_memory = CombinedMemory(
    memories=[chat_buffer_memory, chat_summary_memory]
)

print(chat_combined_memory.aload_memory_variables({}))

chain = LLMChain(llm=ChatOpenAI(),
                 prompt=prompt_template,
                 memory=chat_combined_memory)

print(chain.invoke({'question': "Can you give me an interesting fact I probably didn't know about?"}))

print(chat_combined_memory.aload_memory_variables({})['message_buffer_log'])
print(chat_combined_memory.aload_memory_variables({})['message_summary_log'])