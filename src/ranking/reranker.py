def rerank(results):
    return sorted(results, key=lambda x: x["popularity"], reverse=True)
