import requests
import json

class IntentParser:
    def __init__(self, model="mistral"):
        self.model = model

    def parse(self, query):
        prompt = f"""
Extract structured movie preferences from this query.
Return JSON with:
genres, tone, max_violence

Query: {query}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        text = response.json()["response"]

        try:
            return json.loads(text)
        except:
            return {}
