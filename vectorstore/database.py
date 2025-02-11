import sqlite3

class MetadataDatabase:
    def __init__(self, db_path="vector_store.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)  # ✅ Fix applied here
        self.cursor = self.conn.cursor()
        self._setup_table()

    def _setup_table(self):
        """Create metadata table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS metadata (
                id TEXT PRIMARY KEY,
                text TEXT
            )
        """)
        self.conn.commit()

    def add_metadata(self, doc_id, text):
        """Insert document metadata."""
        self.cursor.execute("INSERT INTO metadata (id, text) VALUES (?, ?)", (doc_id, text))
        self.conn.commit()

    def get_metadata(self, doc_id):
        """Retrieve metadata for a given document ID."""
        self.cursor.execute("SELECT text FROM metadata WHERE id=?", (doc_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        """Close database connection."""
        self.conn.close()
