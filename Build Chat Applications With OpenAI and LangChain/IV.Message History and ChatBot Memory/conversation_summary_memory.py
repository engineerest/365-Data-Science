from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationSummaryMemory
from langchain.globals import set_verbose
set_verbose(True)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwars={'seed': 365},
    temperature=0,
    max_tokens=100
)

# String Template
# A description of the chatbot
# A placeholder for the current conversation
# A placeholder for the human question
# A place holder for the AI response

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

chat_memory = ConversationSummaryMemory(llm=ChatOpenAI(),
                                        memory_key='message_log',
                                        return_messages=False)

# ConversationSummaryMemory -> Summarize the conversation held so far
# LLM -> The language model that will create the summary

# GPT-3.5 Turbo -> Responsible for the summary
# GPT-4 -> Responsible for the conversation

print(chat_memory.load_memory_variables({}))

chain = LLMChain(llm=chat,
                 prompt=prompt_template,
                 memory=chat_memory)

# print(chain.invoke({'question': "Can you give me an interesting fact I probably didn't know about?"}))
print(chain.invoke({'question': "Can you elaborate a bit more on this fact?"}))