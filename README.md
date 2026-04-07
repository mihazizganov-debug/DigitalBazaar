# DigitalBazaar

Интернет-магазин цифровых товаров. Проект разрабатывается в рамках курса по Django.

## Текущий функционал

- Главная страница с каталогом товаров
- Страница контактов с формой обратной связи
- Адаптивный дизайн на Bootstrap 5

## Технологии

- Python 3.x
- Django 6.0.3
- Bootstrap 5
- SQLite (разработка)

## Структура проекта
```

DigitalBazaar/
├── catalog/                                  # Основное приложение
│ ├── migrations/                             # Миграции БД
│ ├── templates/                              # Шаблоны
│ │ └── catalog/
│ │ ├── home.html                             # Главная страница
│ │ └── contacts.html                         # Контакты
│ ├── urls.py                                 # Маршруты приложения
│ ├── views.py                                # Контроллеры
│ └── models.py                               # Модели БД (в разработке)
├── config/                                   # Настройки проекта
│ ├── settings.py                             # Конфигурация Django
│ └── urls.py                                 # Главные маршруты
├── static/                                   # Статические файлы
│ ├── css/
│ └── js/
├── venv/                                     # Виртуальное окружение
├── manage.py                                 # Управляющий скрипт
├── db.sqlite3                                # База данных
├── requirements.txt                          # Зависимости
└── .gitignore                                # Игнорируемые файлы
```

text

## Установка и запуск

1. **Клонировать репозиторий:**
```bash
git clone https://github.com/mihazizganov-debug/DigitalBazaar
DigitalBazaar

Создать и активировать виртуальное окружение:
bash
# Windows
python -m venv venv
venv\Scripts\activate


Установить зависимости:
bash
pip install -r requirements.txt

Применить миграции:
bash
python manage.py migrate

Запустить сервер:
bash
python manage.py runserver


Открыть в браузере:

Главная страница: http://127.0.0.1:8000/

Контакты: http://127.0.0.1:8000/contacts/