from langchain_community.vectorstores import Chroma
from datasets import load_dataset
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import filter_complex_metadata
from typing import List
from tqdm import tqdm

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


    def ingest_olympiads_dataset_to_chromadb(
        self,
        collection_name: str = "pb_solutions",
        max_records: int = 500  # fixe à 500 comme demandé
    ):
        # 1. Charger et mélanger le dataset
        dataset = load_dataset("Blancy/olympiads_math_220k_subset", split="train")
        dataset = dataset.shuffle(seed=42)  # mélange reproductible

        # 2. Limiter au nombre souhaité
        dataset = dataset.select(range(min(max_records, len(dataset))))
        print(f"Nombre de problèmes chargés : {len(dataset)}")

        # 3. Init Chroma
        db = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_dir
        )

        # 4. Transformer en DataFrame
        df = dataset.to_pandas()

        # 5. Ingestion ligne par ligne
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Ingestion dans ChromaDB"):
            text = row["problem"]
            metadata = row[["solution", "answer", "problem_type", "question_type"]].to_dict()
            db.add_texts([text], metadatas=[metadata])

        print(f"Ingestion terminée dans la collection '{collection_name}'.")
