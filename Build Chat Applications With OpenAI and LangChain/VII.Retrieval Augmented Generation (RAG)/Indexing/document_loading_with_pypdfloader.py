from langchain_community.document_loaders import PyPDFLoader
import copy

loader_pdf = PyPDFLoader("Introduction_to_Data_and_Data_Science.pdf")
pages_pdf = loader_pdf.load()
print(len(pages_pdf))

pages_pdf_cut = copy.deepcopy(pages_pdf)

# We want to change the page content of the documents inside pages_pdf_cut by removing all newline characters

print(pages_pdf_cut[0].page_content.split())

print(' '.join(pages_pdf_cut[0].page_content.split()))

for i in pages_pdf_cut:
    i.page_content = ' '.join(i.page_content.split())

print(pages_pdf_cut)

# In this example: The new line characters cluttered the text rather than contributed to the formatting.

# Usually: The newlines can later be used to split the text into meaningful chunks