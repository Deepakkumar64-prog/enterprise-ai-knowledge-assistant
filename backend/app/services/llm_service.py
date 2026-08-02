import requests


class LLMService:

    @staticmethod
    def generate_response(prompt: str):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        return response.json()["response"]