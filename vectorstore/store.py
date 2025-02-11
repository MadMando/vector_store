import numpy as np
import sqlite3

class VectorStore:
    def __init__(self, db_path="vector_store.db", dim=384):
        self.dim = dim
        self.vectors = []  
        self.ids = []  
        self._setup_db(db_path)

    def _setup_db(self, db_path):
        """Initialize SQLite for storing metadata with multi-threading enabled."""
        self.conn = sqlite3.connect(db_path, check_same_thread=False)  # ✅ FIX APPLIED
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS metadata (
                id TEXT PRIMARY KEY,
                text TEXT
            )
        """)
        self.conn.commit()

    def add(self, doc_id, text, embedding):
        """Store vector and metadata."""
        self.ids.append(doc_id)
        self.vectors.append(np.array(embedding, dtype=np.float32))

        self.cursor.execute("INSERT INTO metadata (id, text) VALUES (?, ?)", (doc_id, text))
        self.conn.commit()

    def get_metadata(self, doc_id):
        """Retrieve metadata for a document ID."""
        self.cursor.execute("SELECT text FROM metadata WHERE id=?", (doc_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
