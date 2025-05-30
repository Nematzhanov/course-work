import speech_recognition as sr
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю... Говорите что-нибудь.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {text}")
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса: {e}")
            return None

if __name__ == "__main__":
    speech_to_text()
