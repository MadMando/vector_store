import unittest
from vectorstore.store import VectorStore

class TestVectorStore(unittest.TestCase):
    def setUp(self):
        self.store = VectorStore(dim=384)

    def test_add_and_retrieve_metadata(self):
        self.store.add("doc_1", "Test document", [0.1] * 384)
        metadata = self.store.get_metadata("doc_1")
        self.assertEqual(metadata, "Test document")

if __name__ == "__main__":
    unittest.main()
