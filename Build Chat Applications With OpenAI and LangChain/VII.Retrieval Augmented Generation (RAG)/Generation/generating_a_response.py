from dotenv import load_dotenv

load_dotenv('.env')

from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

vectorstore = Chroma(persist_directory='./intro-to-ds-lectures',
                    embedding_function=OpenAIEmbeddings())

print(len(vectorstore.get()['documents']))

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.7}
)

TEMPLATE = '''
Answer the following question:
{question}

To answer the question, use only the following context:
{context}

At the end of the response, specify the name of the lecture this context is taken from in the format:
Resources: *Lecture Title*
where *Lecture Title* should be substituted with the title of all resource lectures.
'''

prompt_template = PromptTemplate.from_template(TEMPLATE)

chat = ChatOpenAI(
    model_name='gpt-4',
    model_kwargs={'seed': 365},
    max_tokens=250
)

question = "What software do data scientists use?"

chain = ({'context': retriever,
         'question': RunnablePassthrough()}
         | prompt_template
         | chat
         | StrOutputParser())

print(chain.invoke(question))