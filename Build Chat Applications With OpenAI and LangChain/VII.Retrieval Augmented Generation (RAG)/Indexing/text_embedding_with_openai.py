from dotenv import load_dotenv

load_dotenv('.env')

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.markdown import MarkdownTextSplitter
from langchain_text_splitters.character import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
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

# Toy Example
# We'll apply the available embed_query() method on three individual strings.

vector1 = embedding.embed_query(pages_char_split[3].page_content)
vector2 = embedding.embed_query(pages_char_split[5].page_content)
vector3 = embedding.embed_query(pages_char_split[18].page_content)
print(vector1, vector2, vector3)
print(len(vector1), len(vector2), len(vector3))

# We can apply the dot product to each pair of vectors and quantify the similarity

print(np.dot(vector1, vector2), np.dot(vector1, vector3), np.dot(vector2, vector3))

# Vectors 1 and 2 are further apart from vector 3 in this vector space.

# Let's ensure that the vectors created with OpenAI's embedding function have a magnitude of 1

print(np.linalg.norm(vector1), np.linalg.norm(vector2), np.linalg.norm(vector3))