import requests

class ResponseGenerator:
    def __init__(self, model="mistral"):
        self.model = model

    def generate(self, query, recommendations):
        prompt = f"""
User query: {query}

Recommendations:
{recommendations}

Explain why these match the user preferences.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
