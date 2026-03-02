import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, embeddings, metadata):
        self.index.add(embeddings)
        self.metadata.extend(metadata)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        results = [self.metadata[i] for i in indices[0]]
        return results
