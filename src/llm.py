import ollama
import json
from text_finder import text_finder_cos


class gemma_handler:
    def __init__(self) -> None:
        self.finder = text_finder_cos()
        with open("./data/prompt.json") as f:
            d = json.load(f)
        self.q_prompt = d["q"]
        self.q_rag_prompt = d["q_rag"]

    def _get_response(self, prompt: str) -> str:
        response = ollama.chat(
            model="gemma2",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return response["message"]["content"]

    def get_answer(self, question: str) -> str:
        answer = self._get_response(self.q_prompt.format(question))
        return answer

    def get_answer_rag(self, question: str) -> str:
        text = self.finder.find_text(question)
        print(text)
        answer = self._get_response(self.q_rag_prompt.format(question, text))
        return answer
