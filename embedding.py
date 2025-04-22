from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import SingleStoreDB

def embed_to_singlestore(docs, user, pw, host, port, db, table):
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    return SingleStoreDB.from_documents(
        documents=docs,
        embedding=embed_model,
        table_name=table,
        host=host,
        port=int(port),
        user=user,
        password=pw,
        database=db
    )

