from dotenv import load_dotenv

load_dotenv('.env')

from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embedding = OpenAIEmbeddings(model='text-embedding-ada-002')

vectorstore = Chroma(persist_directory='./intro-to-ds-lectures',
                    embedding_function=embedding)

print(len(vectorstore.get()['documents']))

retriever = vectorstore.as_retriever(search_type="mmr",
                                     search_kwargs={"k": 3,
                                                    "lambda_mult": 0.7})
# Number of documents retrieved (k)

# Lambda multiplication factor (lambda_mult)

print(retriever)

question = "What software do data scientists use?"

retrieved_docs = retriever.invoke(question)

for i in retrieved_docs:
    print(f"Page Content: {i.page_content}\n------------\nLecture Title: {i.metadata['Lecture Title']}\n")