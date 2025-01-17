from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import CommaSeparatedListOutputParser

chat = ChatOpenAI(model_name='gpt-4',
                    model_kwargs={'seed': 365},
                    temperature=0,
                    max_tokens=100)

message_h = HumanMessage(content=f'''I've recently adopted a dog. Could you suggest some dog names?

{CommaSeparatedListOutputParser().get_format_instructions()}
''')
# goal: [name1, name2, ...]

print(message_h.content)

response = chat.invoke([message_h])
print(response)

list_output_parser = CommaSeparatedListOutputParser()

response_parsed = list_output_parser.invoke(response)
print(response_parsed)

# goal: [name1, name2, ...]
# result: [content]

# How can we arrive at the desired result?
# By instructing the chat model!

print(list_output_parser.get_format_instructions())