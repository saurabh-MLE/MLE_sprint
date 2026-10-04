import os
import chromadb
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

print("Initializing vector store...")
client = chromadb.PersistentClient(path="./vector_store")
collection = client.get_or_create_collection(name="mle_docs")

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def run_ingestion():
    data_dir = "data"
    print(f"Checking data directory: '{os.path.abspath(data_dir)}'")
    
    if not os.path.exists(data_dir):
        print(f"ERROR: Directory '{data_dir}' not found.")
        return

    files = [f for f in os.listdir(data_dir) if f.endswith(('.txt', '.md'))]
    print(f"Found files in data/: {files}")
    
    if not files:
        print(f"ERROR: No .txt or .md files found in '{data_dir}'.")
        return

    for filename in files:
        filepath = os.path.join(data_dir, filename)
        print(f"Processing file: {filepath}")
        
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()

        chunks = chunk_text(raw_text)
        print(f"Generated {len(chunks)} chunks.")
        if not chunks:
            continue

        print(f"Embedding {len(chunks)} chunks from {filename}...")
        embeddings = embedder.encode(chunks).tolist()
        ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]
        metadatas = [{"source": filename, "chunk_index": i} for i in range(len(chunks))]

        collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )
        print(f"Successfully upserted {len(chunks)} chunks into ChromaDB from {filename}.")

if __name__ == "__main__":
    run_ingestion()