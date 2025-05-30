import requests

API_KEY = "" #ваш API
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_qwen(prompt):
    data = {
        "model": "qwen-v1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    user_prompt = "Привет! Как дела?"
    try:
        answer = ask_qwen(user_prompt)
        print("Ответ Qwen:", answer)
    except Exception as e:
        print("Ошибка при запросе:", e)
