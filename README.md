# DjangoProject1 — Уведомления о статусе задач

Проект создан в рамках курса **Python Advanced**. Основная цель — реализовать механизм отправки email-уведомлений при изменении статуса задач с помощью Django сигналов.

---

## 📌 Функционал

- Модель `Task` с полями: `title`, `status`, `owner`, `last_notified_status`
- Сигнал `post_save` отслеживает изменение статуса задачи
- Если статус изменился, пользователю отправляется уведомление (в консоль)
- Проверка: уведомление не дублируется, если статус не изменился

---

## 🔔 Пример шаблона уведомления

text
📧 Email to user@example.com: Task "HomeWork" changed status to DONE!

--------------------------------------------------------------------------

⚙️ Технологии
Python 3.13

Django 5.2

Email backend: console.EmailBackend

Django signals (post_save)

SQLite (по умолчанию)

--------------------------------------------------------------------------

📦 Установка
git clone https://github.com/VitalijsFilipovs/DjangoProject1.git
cd DjangoProject1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

--------------------------------------------------------------------------

🧪 Тестирование
Зайди в Django admin: http://127.0.0.1:8000/admin/

Создай пользователя и задачу

Измени статус задачи

Уведомление появится в консоли


