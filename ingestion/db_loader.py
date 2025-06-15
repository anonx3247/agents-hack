from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
import re
import uuid

class VectorStoreLoader:
    def __init__(self, persist_dir: str, embedding_model: str):
        print(f"Initializing vector store at: {persist_dir}")
        self.persist_dir = persist_dir
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

    def add_documents(self, documents: List[str], metadata: dict = None, collection_name: str = "default"):

        db = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_dir
        )
        print(f"Inserting {len(documents)} document(s) into vector store")
        db.add_texts(documents, metadatas=[metadata] * len(documents) if metadata else None)

        # for doc in documents:
        #     print(f"Content: {doc[:50]}...")
        #     print("Documents added to vector store.")   

        db.persist()
        print(f"Vector store persisted into {collection_name} collection")
