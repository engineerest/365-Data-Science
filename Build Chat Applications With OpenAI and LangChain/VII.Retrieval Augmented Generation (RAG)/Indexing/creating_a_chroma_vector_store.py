from dotenv import load_dotenv

load_dotenv('.env')

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import numpy as np

loader_docx = Docx2txtLoader("Introduction_to_Data_and_Data_Science_2.docx")
pages = loader_docx.load()

md_splitter = MarkdownTextSplitter(
    headers_to_split_on=[("#", "Course Title"),
                         ("##", "Lecture Title")]
)

pages_md_split = md_splitter.split_text(pages[0].page_content)

for i in range(len(pages_md_split)):
    pages_md_split[i].page_content = ' '.join(pages_md_split[i].page_content.split())

char_splitter = CharacterTextSplitter(
    separator='.',
    chunk_size=500,
    chunk_overlap=50
)

pages_char_split = char_splitter.split_documents(pages_md_split)
print(pages_char_split)

embedding = OpenAIEmbeddings(model='text-embedding-ada-002')

print(pages_char_split[18])

vector_store = Chroma.from_documents(documents=pages_char_split,
                                     embedding=embedding,
                                     persist_directory="./intro-to-ds-lectures")
# We want this vector store to keep all 20 documents from the pages_char_split list and their vector representations

# persist_directory is not a required parameter
# If you don't specify it, the vectorstore will only exist
# until the kernel is restarted or shut down

# Persisting a vector collection allows us to retrieve it even if we restart the kernel.

# This avoid embedding all tokens anew

vectorstore_from_directory = Chroma(persist_directory='./intro-to-ds-lecture',
                                    embedding_function=embedding)
# The documents in the vector store can be updated, or new ones can be added

# The vectorstore needs to know which embedding function to use to maintain consistency and accuracy
# in the representation of existing and newly added documents