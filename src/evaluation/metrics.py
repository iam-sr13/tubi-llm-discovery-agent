def precision_at_k(results, target_genre, k=5):
    hits = 0
    for r in results[:k]:
        if r["genre"].lower() == target_genre.lower():
            hits += 1
    return hits / k
