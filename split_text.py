from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

def split_text_to_chunks(text, chunk_size=1000, overlap=100):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return [Document(page_content=chunk) for chunk in splitter.split_text(text)]
