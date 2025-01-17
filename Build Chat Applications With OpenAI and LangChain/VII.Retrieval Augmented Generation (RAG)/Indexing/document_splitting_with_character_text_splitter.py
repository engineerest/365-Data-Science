from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters.character import CharacterTextSplitter

loader = Docx2txtLoader("Introduction_to_Data_and_Data_Science.docx")
pages = loader.load()
for i in range(len(pages)):
    pages[i].page_content = ' '.join(pages[i].page_content.split())

print(pages[0].page_content)
print(len(pages[0].page_content))

char_splitter = CharacterTextSplitter(separator='',
                                      chunk_size=500,
                                      chunk_overlap=50)
# chunk_overlap default value is 200 characters

pages_char_split = char_splitter.split_documents(pages)
print(pages_char_split)
print(len(pages_char_split))

print(pages_char_split[0].page_content)

print(8259/500)

print(0.518*500)

print(len(pages_char_split[16].page_content))