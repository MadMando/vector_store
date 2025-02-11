import numpy as np
from scipy.spatial.distance import cosine

class VectorSearch:
    def __init__(self, store):
        self.store = store

    def search(self, query_embedding, top_k=3):
        """Find the top K most similar vectors."""
        if not self.store.vectors:
            return []

        query_vec = np.array(query_embedding, dtype=np.float32)
        scores = [1 - cosine(query_vec, vec) for vec in self.store.vectors]

        top_indices = np.argsort(scores)[::-1][:top_k]
        return [(self.store.ids[i], self.store.get_metadata(self.store.ids[i]), scores[i]) for i in top_indices]
