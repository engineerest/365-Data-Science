from langchain.prompts import PromptTemplate

TEMPLATE = '''
System:
{description} 

Human:
I've recently adopted a {pet}.
Could you suggest some {pet} names?
''' # Character description placeholder for the chatbot to impersonate

prompt_template = PromptTemplate.from_template(template=TEMPLATE)
print(prompt_template)


# invoke()
# Class             Accepts             Returns
# PromptTemplate    Dictionary          PromptValue
# ChatOpenAI        String              AIMessage
#                   List of chat
#                   messages

prompt_value = prompt_template.invoke({'description': '''The chatbot should reluctantly answer questions 
with sarcastic responses.''', 'pet':'dog'})
print(prompt_value)

print(prompt_value.text)