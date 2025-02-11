import argparse
from sentence_transformers import SentenceTransformer
from vector_store.store import VectorStore
from vector_store.database import MetadataDatabase

# Initialize models
embedder = SentenceTransformer("all-MiniLM-L6-v2")
store = VectorStore()
db = MetadataDatabase()

def add_document(doc_id, text):
    embedding = embedder.encode(text).tolist()
    store.add(doc_id, text, embedding)
    db.add_metadata(doc_id, text)
    print(f"Document {doc_id} added successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add documents to vector store.")
    parser.add_argument("--id", type=str, required=True, help="Document ID")
    parser.add_argument("--text", type=str, required=True, help="Document content")
    args = parser.parse_args()

    add_document(args.id, args.text)
