from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.messages import AIMessage

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    temperature=0,
    max_tokens=100
)

message_s = SystemMessage(content='''You are Marv, a chatbot that reluctantly answers questions with sarcastic responses.''')
message_h = HumanMessage(content='''I've recently adopted a dog. Can you suggest some dog names?''')

response = chat.invoke([message_s, message_h])# -> String [Chat Messages]

print(response)

print(response.content)

message_h_dog = HumanMessage(content='''I've recently adopted a dog. Could you suggest some dog names?''')
message_ai_dog = AIMessage(content='''Oh, absolutely, Because nothing screams "I'm a responsible pet owner"
like asking a chatbot to name your new furball. How about "Bark Twain" (if it's a literary hound)?''')

message_h_cat = HumanMessage(content='''I've recently adopted a cat. Could you suggest some cat names?''')
message_ai_cat = AIMessage(content='''Oh, absolutely, Because nothing screams "I'm a responsible pet owner"
like asking a chatbot to name your new furball. How about "Bark Twain" (if it's a literary hound)?''')

message_h_fish = HumanMessage(content='''I've recently adopted a fish. Could you suggest some fish names?''')

response = chat.invoke([message_h_dog, message_ai_dog, message_h_cat, message_h_fish])


print(response)

print(response.content)