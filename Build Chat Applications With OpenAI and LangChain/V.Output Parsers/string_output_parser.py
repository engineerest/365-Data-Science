from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI(model_name='gpt-4',
                    model_kwargs={'seed': 365},
                    temperature=0,
                    max_tokens=100)

message_h = HumanMessage(content="Can you give me an interest fact I probably didn't know about?")

response = chat.invoke([message_h])

print(response)

str_output_parser = StrOutputParser()
response_parsed = str_output_parser.invoke(response)
print(response_parsed)
