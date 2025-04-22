import os
from scrape import scrape_url_text
from split_text import split_text_to_chunks
from embedding import embed_to_singlestore
from watsonx_model import get_granite_llm
from rag_chain import create_rag_chain

# ⬇️ Load env or hardcode creds here
user="admin"
pw="qfbk|azMenmObmpx;7G1d;:e"
host=os.getenv("SINGLESTORE_HOST")
port=3306
db ="rag_db"
table = "webpage_embeddings"

# 1. Scrape
text = scrape_url_text("https://en.wikipedia.org/wiki/Retrieval-augmented_generation")

# 2. Chunk
docs = split_text_to_chunks(text)

# 3. Embed to Vector Store
vectorstore = embed_to_singlestore(docs, user, pw, host, port, db, table)

# 4. Watsonx LLM
llm = get_granite_llm()

# 5. Build RAG Chain
qa = create_rag_chain(llm, vectorstore)

# 6. Ask Question
query = "What is retrieval-augmented generation?"
answer = qa.run(query)
print("Answer:", answer)
