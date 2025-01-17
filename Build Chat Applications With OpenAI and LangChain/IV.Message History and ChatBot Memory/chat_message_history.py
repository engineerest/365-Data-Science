from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain.prompts import (ChatPromptTemplate,
                               HumanMessagePromptTemplate,)

from langchain.chains.llm import LLMChain

from langchain_community.chat_message_histories import ChatMessageHistory

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

background_info = ChatMessageHistory()
print(background_info)

background_info.add_user_message("Can you give interesting fact I probably didn't know about?") # Append a human message to the list
background_info.add_ai_message("Sure, did you know that the longest place name on the planet is 85 letters long?")

print(background_info)

# ChatMessageHistory vs List

# Advantages of ChatMessageHistory
# Converting to various formats
# background_info.json()
# background_info.dict()
# background_info.schema()
# Quickly clearing chat histories
# background_info.clear()
# Integrating it with a LangChain memory object

message_template_h = HumanMessagePromptTemplate.from_template(template='{follow-up question}')
chat_template = ChatPromptTemplate.from_messages(background_info.messages + [message_template_h]) # Concatenates lists

print(chat_template)

chain = LLMChain(llm=chat, prompt=chat_template)

response = chain.invoke({'follow-up question': 'What is the name?'})
print(response)

print(response['text'])

response = chain.invoke({'follow-up question': 'What is the name mean?'})
print(response)

print(response['text'])

# The ChatMessageHistory class is suitable for situations where
# we need to manage history messages outside a chain

# When recollecting messages from the current conversation,
# we should instead turn to memory classes.