from dotenv import load_dotenv

load_dotenv('.env')

from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embedding = OpenAIEmbeddings(model='text-embedding-ada-002')

vectorstore = Chroma(persist_directory='./intro-to-ds-lectures',
                    embedding_function=embedding)

added_document = Document(page_content='Alright! So… Let’s discuss the not-so-obvious differences between the terms analysis and analytics. Due to the similarity of the words, some people believe they share the same meaning, and thus use them interchangeably. Technically, this isn’t correct. There is, in fact, a distinct difference between the two. And the reason for one often being used instead of the other is the lack of a transparent understanding of both. So, let’s clear this up, shall we? First, we will start with analysis',
                          metadata={'Course Title': 'Introduction to Data and Data Science',
                                    'Lecture Title': 'Analysis vs Analytics'})

print(vectorstore.add_documents([added_document]))

question = "What programming language is used in data science?"

retrieved_docs = vectorstore.max_marginal_relevance_search(
    query=question,
    k=3,
    lambda_mult=0.1,
    filter={'Lecture Title': "Programming Languages & Software Employed in Data Science - All the Tools You Need"}
)

for i in retrieved_docs:
    print(f"Page Content: {i.page_content}\n------------\nLecture Title: {i.metadata['Lecture Title']}\n")