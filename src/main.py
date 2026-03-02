from fastapi import FastAPI
import pandas as pd
from src.retrieval.embeddings import EmbeddingModel
from src.retrieval.vector_store import VectorStore
from src.llm.intent_parser import IntentParser
from src.llm.response_generator import ResponseGenerator
from src.ranking.reranker import rerank

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

movies = pd.read_csv("data/movies_sample.csv")

embedding_model = EmbeddingModel()
embeddings = embedding_model.encode(movies["description"].tolist())

vector_store = VectorStore(embeddings.shape[1])
vector_store.add(embeddings, movies.to_dict(orient="records"))

intent_parser = IntentParser()
response_generator = ResponseGenerator()

@app.get("/recommend")
def recommend(query: str):
    prefs = intent_parser.parse(query)
    logger.info(f"Received query: {query}")
    logger.info(f"Parsed preferences: {prefs}")

    query_embedding = embedding_model.encode([query])
    results = vector_store.search(query_embedding, k=5)

    ranked = rerank(results)

    explanation = response_generator.generate(query, ranked)

    return {
        "recommendations": ranked,
        "explanation": explanation
    }
