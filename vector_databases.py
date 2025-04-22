from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import logging

# Suppress CropBox Warnings
logging.getLogger("pdfplumber").setLevel(logging.ERROR)

pdfs_directory = "pdfs/"

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    print("[*] Loading PDF...")
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    print(f"[+] Loaded {len(documents)} pages.")
    return documents

def create_chunks(documents):
    print("[*] Splitting into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)
    print(f"[+] Created {len(text_chunks)} chunks.")
    return text_chunks

def get_embedding_model(model_name):
    print(f"[*] Loading embedding model: {model_name}")
    return OllamaEmbeddings(model=model_name)

def create_vector_store(chunks, embedding_model):
    print("[*] Creating FAISS vector store...")
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local("vectorstore/db_faiss")
    print("[+] Vector store saved at vectorstore/db_faiss")

# Main
file_path = 'data.pdf'
documents = load_pdf(file_path)
text_chunks = create_chunks(documents)
embedding_model = get_embedding_model("deepseek-r1:1.5b")
create_vector_store(text_chunks, embedding_model)
