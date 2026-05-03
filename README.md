# DigitalBazaar

Интернет-магазин цифровых товаров. Проект разрабатывается в рамках курса по Django.

## Текущий функционал

- Главная страница со списком товаров из БД (CBV)
- Страница детального просмотра товара (CBV)
- Страница контактов с формой обратной связи (CBV)
- **CRUD для товаров (создание, редактирование, удаление)**
- **Валидация форм (запрещённые слова, отрицательная цена)**
- **Стилизация форм Bootstrap**
- Блог с полным CRUD (создание, чтение, обновление, удаление)
- Счётчик просмотров статей блога
- Фильтрация опубликованных статей
- Базовый шаблон и подшаблоны (меню, подвал)
- Адаптивный дизайн на Bootstrap 5
- Подключена PostgreSQL
- Модели Product и Category с миграциями
- Админ-панель для управления товарами и блогом
- Фикстуры для загрузки тестовых данных
- Кастомная команда `load_data`

## Технологии

- Python 3.13
- Django 6.0.3
- PostgreSQL 18
- Bootstrap 5
- ipython 9.12.0
- Pillow 12.2.0

## Структура проекта
```

DigitalBazaar/
├── blog/                                     # Приложение блога
│ ├── migrations/                             # Миграции блога
│ ├── templates/                              # Шаблоны блога
│ │ └── blog/
│ │  ├── blog_list.html                       # Список статей
│ │  ├── blog_detail.html                     # Детальная страница
│ │  ├── blog_form.html                       # Создание/редактирование
│ │  └── blog_confirm_delete.html             # Подтверждение удаления
│ ├── admin.py                                # Регистрация моделей
│ ├── models.py                               # Модель BlogPost
│ ├── urls.py                                 # Маршруты блога
│ └── views.py                                # CBV для блога
│
├── catalog/                                  # Основное приложение
│ ├── fixtures/                               # Фикстуры для БД
│ │ ├── categories.json                       # Данные категорий
│ │ └── products.json                         # Данные продуктов
│ ├── management/                             # Кастомные команды
│ │ └── commands/
│ │  └── load_data.py                         # Команда загрузки данных
│ ├── migrations/                             # Миграции БД
│ ├── templates/                              # Шаблоны
│ │ └── catalog/
│ │  ├── base.html                            # Базовый шаблон
│ │  ├── product_detail.html                  # Страница товара
│ │  ├── home.html                            # Главная страница
│ │  ├── contacts.html                        # Контакты
│ │  ├── product_confirm_delete.html          # Подтверждение удаления   (новое)
│ │  ├── product_form.html                    # Форма создания/редактирования  (новое)
│ │  └── includes/
│ │    ├── navbar.html                        # Подшаблон меню
│ │    └── footer.html                        # Подшаблон подвала
│ ├── urls.py                                 # Маршруты приложения
│ ├── views.py                                # Контроллеры
│ └── models.py                               # Модели БД
│
├── config/                                   # Настройки проекта
│ ├── settings.py                             # Конфигурация Django
│ └── urls.py                                 # Главные маршруты
│
├── static/                                   # Статические файлы
│ ├── css/
│ └── js/
├── screenshots/                              # Скриншоты для проверки
├── venv/                                     # Виртуальное окружение
├── manage.py                                 # Управляющий скрипт
├── requirements.txt                          # Зависимости
├── .gitignore                                # Игнорируемые файлы
├── .env                                      # Переменные окружения (не в git)  
├── .env.example                              # Шаблон переменных окружения
└── LICENSE                                   # Лицензия MIT
  
```

text

## Установка и запуск

1. **Клонировать репозиторий:**
```bash
git clone https://github.com/mihazizganov-debug/DigitalBazaar
cd DigitalBazaar

Создать и активировать виртуальное окружение:
bash
# Windows
python -m venv venv
venv\Scripts\activate


Установить зависимости:
bash
pip install -r requirements.txt


Настроить переменные окружения:
Скопируйте .env.example в .env и укажите свои данные PostgreSQL:
DB_NAME=digitalbazaar_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432


Создать базу данных PostgreSQL
Через pgAdmin или командную строку:
CREATE DATABASE digitalbazaar_db;


Применить миграции:
bash
python manage.py migrate


Загрузить тестовые данные:
python manage.py loaddata catalog/fixtures/categories.json catalog/fixtures/products.json


Создать суперпользователя:
python manage.py createsuperuser


Запустить сервер:
bash
python manage.py runserver


Открыть в браузере:

+ Главная страница (список товаров): http://127.0.0.1:8000/

+ Страница товара: http://127.0.0.1:8000/product/1/
  Контакты: http://127.0.0.1:8000/contacts/
  Блог: http://127.0.0.1:8000/blogs/            (new)
  Админ-панель: http://127.0.0.1:8000/admin/

CRUD для товаров

Создать товар: http://127.0.0.1:8000/product/create/

Редактировать: на странице товара → "Редактировать"

Удалить: на странице товара → "Удалить"


Лицензия
MIT License

Copyright (c) 2026 Михаил Зизганов