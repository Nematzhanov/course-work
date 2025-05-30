import requests

API_URL = "https://api.intelligence.io.solutions/api/v1/chat/completions"
API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ваш API"
}

chat_history = [
    {"role": "system", "content": "You are a helpful assistant"}
]

def clean_bot_response(response):
    """Очищает ответ от тегов <think> и форматирования"""
    if '<think>' in response:
        parts = response.split('</think>', 1)
        response = parts[1].strip() if len(parts) > 1 else response
    return response.replace('**', '').strip()

def get_bot_response(user_input):
    """Отправляет запрос к API и возвращает очищенный ответ"""
    try:
        #историю диалога
        chat_history.append({"role": "user", "content": user_input})
        
        # Формируем запрос
        payload = {
            "model": "deepseek-ai/DeepSeek-R1",
            "messages": chat_history
        }
        
        # Отправляем запрос
        response = requests.post(API_URL, headers=API_HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        #очищаем ответ
        bot_response = data['choices'][0]['message']['content']
        cleaned_response = clean_bot_response(bot_response)
        
        # Обновляем историю
        chat_history.append({"role": "assistant", "content": cleaned_response})
        return cleaned_response
        
    except Exception as e:
        return f"Ошибка: {str(e)}"