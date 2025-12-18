from ollama import chat, ChatResponse
import requests


user_query = "малярия"
LLM_API_KEY = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen:7b",
    "prompt": f"""
        Ты эксперт по классификации тем. Проанализируй следующий запрос пользователя и определи его основную тему.

        Запрос: {user_query}

        Инструкции:
        1. Определи одну основную тему (1 слово, например: "Программирование", "Рецепты", "Фитнес").
        2. Не давай дополнительных объяснений, ответ должен содержать строго одно единственное слово.
    """,
    "stream": False,
}

print(requests.post(LLM_API_KEY, json=payload).json().get("response"))