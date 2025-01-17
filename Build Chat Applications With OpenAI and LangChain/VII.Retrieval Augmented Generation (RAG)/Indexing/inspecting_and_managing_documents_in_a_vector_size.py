from dotenv import load_dotenv

load_dotenv('.env')

from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

embedding = OpenAIEmbeddings(model='text-embedding-ada-002')

vectorstore_from_directory = Chroma(persist_directory='./intro-to-ds-lectures',
                                    embedding_function=embedding)

print(vectorstore_from_directory.get())
print(vectorstore_from_directory.get(ids="00829d7d-4ad7-4f83-93c2-1c606f3c14bf",
                                     include=['embeddings']))

added_document = Document(page_content='Alright! So… Let’s discuss the not-so-obvious differences between the terms analysis and analytics. Due to the similarity of the words, some people believe they share the same meaning, and thus use them interchangeably. Technically, this isn’t correct. There is, in fact, a distinct difference between the two. And the reason for one often being used instead of the other is the lack of a transparent understanding of both. So, let’s clear this up, shall we? First, we will start with analysis',
                          metadata={'Course Title': 'Introduction to Data and Data Science',
                                    'Lecture Title': 'Analysis vs Analytics'})

print(vectorstore_from_directory.add_documents([added_document]))

print(vectorstore_from_directory.get("55409552-1943-4892-949a-3b475ff9c840"))

updated_document = Document(page_content='Great! We hope we gave you a good idea about the level of applicability of the most frequently used programming and software tools in the field of data science. Thank you for watching!',
                            metadata={'Course Title': 'Introduction to Data and Data Science',
                                     'Lecture Title': 'Programming Languages & Software Employed in Data Science - All the Tools You Need'})

print(vectorstore_from_directory.update_document(
    document_id="55409552-1943-4892-949a-3b475ff9c840",
    document=updated_document
))

print(vectorstore_from_directory.get("55409552-1943-4892-949a-3b475ff9c840"))

print(vectorstore_from_directory.delete("55409552-1943-4892-949a-3b475ff9c840"))

print(vectorstore_from_directory.get("55409552-1943-4892-949a-3b475ff9c840"))