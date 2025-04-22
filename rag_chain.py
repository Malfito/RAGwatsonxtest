from langchain.chains import RetrievalQA

def create_rag_chain(llm, vectorstore, k=5):
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
