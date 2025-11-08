# Chat Jigit — README

Проект состоит из двух модулей:

* **`chat_api.py`** — отвечает за обращение к API-модели на сайте [ai.io.net](https://ai.io.net).
* **`UI.py`** — пользовательский интерфейс на **Flet**, который использует `chat_api` для общения с моделью.

---

## 🚀 Что делает проект

Chat Jigit — это простой интерфейс для общения с нейросетью с сайта [ai.io.net](https://ai.io.net).
Пользователь вводит сообщение в окне приложения, а ответ приходит от модели через API-запрос.

---

## ⚙️ Требования

* **Python 3.10+**
* **Git** (если проект клонируется)
* Рекомендуется создать виртуальное окружение (venv)

---

## 🧩 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone git@github.com:Nematzhanov/course-work.git
cd course-work
```

### 2. Создать виртуальное окружение

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

Создай файл `requirements.txt` со следующим содержимым:

```
flet
requests
pyperclip
```

Затем установи библиотеки:

```bash
pip install -r requirements.txt
```

---

## 🔑 Получение API-ключа

Чтобы приложение работало, нужен **API-ключ от сайта [ai.io.net](https://ai.io.net)**.

### Как получить ключ:

1. Перейди на сайт: [https://ai.io.net](https://ai.io.net)
2. Зарегистрируйся или войди в свой аккаунт.
3. Найди раздел **API Keys** или **Developer API**.
4. Скопируй свой **API-ключ**.
5. Вставь его в `chat_api.py` в строку:

   ```python
   "Authorization": "Bearer ВАШ_API_КЛЮЧ"
   ```

> ⚠️ Ключ должен выглядеть примерно так:
>
> ```
> io-v2-xxxxxxxxxxxxxxxxxxxx
> ```

Если ты не вставишь ключ, приложение не сможет отправлять запросы к модели.

---

## 💻 Запуск приложения

После того как ключ добавлен:

```bash
python UI.py
```

Приложение откроется в отдельном окне.

---

## 📁 Структура проекта

```
course-work/
├─ chat_api.py      # Логика взаимодействия с API
├─ UI.py            # Интерфейс пользователя
├─ requirements.txt # Список зависимостей
├─ README.md        # Этот файл
└─ .gitignore
```

---
Nematzhanov Mukhammadzakhid<br/>
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?logo=telegram&logoColor=white)](https://t.me/nematzhonov)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/nematzhanov_?igsh=NTc4MTIwNjQ2YQ==)
[![VK](https://img.shields.io/badge/VK-0077FF?logo=vk&logoColor=white)](https://vk.com/nematzhanov_m)
