from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI(
    title="Local RAG Engine API",
    description="In-process RAG pipeline using ChromaDB, Sentence-Transformers, and Flan-T5-Small",
    version="1.0.0"
)

print("Initializing RAG Pipeline components...")

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./vector_store")
collection = client.get_collection(name="mle_docs")

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
print("RAG Pipeline initialization complete.")

class QueryRequest(BaseModel):
    question: str
    top_k: int = 2

class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "vector_store_chunks": collection.count()
    }

@app.post("/rag/query", response_model=QueryResponse)
def query_rag_endpoint(payload: QueryRequest):
    try:
        query_vector = embedder.encode([payload.question]).tolist()

        results = collection.query(
            query_embeddings=query_vector,
            n_results=payload.top_k
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            return QueryResponse(
                question=payload.question,
                answer="No relevant context found.",
                sources=[]
            )

        context = "\n---\n".join(documents)
        prompt = (
            f"Context:\n{context}\n\n"
            f"Question: {payload.question}\n\n"
            "Answer the question based only on the context above."
        )

        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(**inputs, max_new_tokens=128)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return QueryResponse(
            question=payload.question,
            answer=answer,
            sources=[meta.get("source") for meta in metadatas if meta]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))