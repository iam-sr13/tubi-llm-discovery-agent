import pandas as pd
from src.evaluation.metrics import precision_at_k

# dummy example
results = [
    {"genre": "Thriller"},
    {"genre": "Thriller"},
    {"genre": "Romance"},
]

print("Precision@3:", precision_at_k(results, "Thriller", 3))
