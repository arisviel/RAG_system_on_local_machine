import ollama
import json
from text_finder import text_finder_cos


class gemma_handler:
    """ Основной класс функий RAG, поднимает модели эмбединга и llm"""
    def __init__(self) -> None:
        """Объявления класса поисковика ближайших отрезков текста и чтение промптов для запросов"""
        self.finder = text_finder_cos()
        with open("./data/prompt.json") as f:
            d = json.load(f)
        self.q_prompt = d["q"]
        self.q_rag_prompt = d["q_rag"]

    def _get_response(self, prompt: str) -> str:
        """Получение ответа ответа от llm"""
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
        """Обработка промпта без раг"""
        answer = self._get_response(self.q_prompt.format(question))
        return answer

    def get_answer_rag(self, question: str) -> str:
        """Обаботка промпта с поиском текстов"""
        text = self.finder.find_text(question)
        answer = self._get_response(self.q_rag_prompt.format(question, text))
        return answer
