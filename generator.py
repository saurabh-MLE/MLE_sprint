import chromadb
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Loading retrieval components...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./vector_store")
collection = client.get_collection(name="mle_docs")
print(f"Toatal chunks in ChromaDB: {collection.count()}")

print("Loading local generation LLM (google/flan-t5-small)...")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def query_rag(question: str, top_k: int = 2) -> dict:
    query_vector = embedder.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_vector,
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "question": question,
            "answer": "No relevant context found.",
            "sources": []
        }

    context = "\n---\n".join(documents)
    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer the question based only on the context above."
    )

    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=128)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "question": question,
        "answer": answer,
        "sources": [meta.get("source") for meta in metadatas]
    }

if __name__ == "__main__":
    test_question = "What prevents per-request disk read latency?"
    print(f"\nTesting Query: '{test_question}'\n")
    output = query_rag(test_question)
    print("Result:")
    print(output)