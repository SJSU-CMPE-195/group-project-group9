import chromadb
from ollama import chat
from ollama import ChatResponse
from pypdf import PdfReader
#client = chromadb.PersistentClient(path="./")
#collection = client.get_or_create_collection("collection")

document = PdfReader('./static/constitution.pdf')
text = document.pages[3].extract_text().replace("\n", "")
print(text)
list = text.split("\n")
ind = text.find("To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries;")
print(ind)
    




