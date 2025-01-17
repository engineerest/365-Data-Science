from langchain_community.document_loaders import Docx2txtLoader

loader_docx = Docx2txtLoader("Introduction_to_Data_and_Data_Science.pdf")
pages_docx = loader_docx.load()

print(pages_docx)