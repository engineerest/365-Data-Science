from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.output_parsers import DatetimeOutputParser

chat = ChatOpenAI(model_name='gpt-4',
                    model_kwargs={'seed': 365},
                    temperature=0,
                    max_tokens=100)

message_h = HumanMessage(content=f'''When was the Danish poet Piet Heinen born?
{DatetimeOutputParser().get_format_instructions()}
''')

print(message_h.content)

response = chat.invoke([message_h])
print(response)

date_output_parser = DatetimeOutputParser()

response_parsed = date_output_parser.invoke(response)
print(response_parsed) # error

print(date_output_parser.get_format_instructions())

# December 16, 1905

# It wouldn't be in the format needed for the parser to transform it to a datetime object.