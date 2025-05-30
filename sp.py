from gtts import gTTS
from playsound import playsound
import os
import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def speak_google(text, lang='ru'):
    filename = "output.mp3" 
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print(f"Ошибка при синтезе или воспроизведении речи: {e}")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except Exception as e:
                print(f"Не удалось удалить временный аудиофайл {filename}: {e}")


if __name__ == "__main__":
    print("Тест синтеза речи.")
    speak_google("Привет! Как твои дела? Это проверка работы синтезатора речи.")
    speak_google("Проверка русского текста прошла успешно.")