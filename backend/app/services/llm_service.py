import requests


class LLMService:

    @staticmethod
    def generate_response(question: str):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": question,
                "stream": False
            },
            timeout=60
        )

        result = response.json()

        return result["response"]