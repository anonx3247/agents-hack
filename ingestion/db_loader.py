from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List

class VectorStoreLoader:
    def __init__(self, persist_dir: str, embedding_model: str):
        print(f"Initializing vector store at: {persist_dir}")
        self.persist_dir = persist_dir
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.db = Chroma(embedding_function=self.embeddings, persist_directory=self.persist_dir)

    def add_documents(self, documents: List[str], metadata: dict = None):
        print(f"Inserting {len(documents)} document(s) into vector store")
        self.db.add_texts(documents, metadatas=[metadata] * len(documents) if metadata else None)
        self.db.persist()
        print("Vector store persisted.")