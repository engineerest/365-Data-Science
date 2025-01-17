from dotenv import load_dotenv

load_dotenv('.env')

from langchain.chat_models import ChatOpenAI

from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    AIMessagePromptTemplate,
                                    FewShotChatMessagePromptTemplate)

chat = ChatOpenAI(model_name='gpt-4',
                  model_kwargs={'seed': 365},
                  temperature=0,
                  max_tokens=100)

TMEPLATE_H = '''I've recently adopted a {pet}. Could you suggest some {pet} names?'''
TEMPLATE_AI = '''{response}'''

message_template_h = HumanMessagePromptTemplate.from_template(template=TMEPLATE_H)
message_template_ai = AIMessagePromptTemplate.from_template(template=TEMPLATE_AI)

example_template = ChatPromptTemplate.from_messages([message_template_h,
                                                     message_template_ai])

# The blueprint for our human-AI example pairs

examples = [{'pet': 'dog',
             'response':'''Oh, absolutely, Because nothing screams "I'm a responsible pet owner"
             like asking a chatbot to name your new furball. How about "Bark Twain" (if it's a literary hound)?')'''},

            {'pet': 'cat',
             'response': '''Oh, absolutely, Because nothing screams "I'm a unique and creative individual"
             like asking a chatbot to name your cat. How about "Furry McFurFace", "Sit Meowsalot", or "Catastrophe"?'''},

            {'pet': 'fish',
             'response': '''Oh, absolutely, Because nothing screams "I'm a responsible pet owner"
             like asking a chatbot to name your fish. How about "Fin Diesel", "Gill Gates", or "Bubbles"?'''},]

few_shot_prompt = FewShotChatMessagePromptTemplate(example=examples,
                                                   example_prompt=example_template)

# Please, also include the following required parameter:
# input_variables=['pet']

chat_template = ChatPromptTemplate.from_messages([few_shot_prompt,
                                                  message_template_h])

chat_value = chat_template.invoke({'pet': 'rabbit'})
print(chat_value)

for i in chat_value.messages:
    print(f'{i.type}: {i.content}\n')

response = chat.invoke(chat_value)
print(response)

# This approach avoids defining a series of message objects and instead uses only a handful of prompt templates