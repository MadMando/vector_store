from fastapi import FastAPI
from pydantic import BaseModel
from vectorstore.store import VectorStore
from vectorstore.search import VectorSearch
from sentence_transformers import SentenceTransformer

app = FastAPI()
store = VectorStore()
search = VectorSearch(store)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

class Document(BaseModel):
    doc_id: str
    text: str

class Query(BaseModel):
    query: str

@app.post("/add/")
def add_document(doc: Document):
    try:
        embedding = embedder.encode(doc.text).tolist()
        store.add(doc.doc_id, doc.text, embedding)
        return {"message": "Document added"}
    except Exception as e:
        print(f"🔥 ERROR in /add/: {str(e)}")  # Prints error in the terminal
        return {"error": str(e)}


@app.post("/search/")
def search_documents(query: Query, top_k: int = 3):
    """Search for similar documents using embeddings"""
    try:
        print(f"Received query: {query.query}, top_k: {top_k}")  # Debugging output

        # Generate embedding
        embedding = embedder.encode(query.query).tolist()
        print(f"Generated embedding: {embedding[:5]}...")  # Print first 5 values

        # Perform search
        results = search.search(embedding, top_k=top_k)
        print(f"Search results: {results}")

        return {"results": results}

    except Exception as e:
        print(f"🔥 ERROR in /search/: {str(e)}")
        return {"error": str(e)}

