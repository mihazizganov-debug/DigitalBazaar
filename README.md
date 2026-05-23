# DigitalBazaar

Интернет-магазин цифровых товаров. Проект разрабатывается в рамках курса по Django.

## Текущий функционал

- Главная страница со списком товаров из БД (CBV)
- Страница детального просмотра товара (CBV)
- Страница контактов с формой обратной связи (CBV)
- **CRUD для товаров (создание, редактирование, удаление) — доступно только авторизованным**
- **Регистрация и авторизация пользователей (по email)**
- **Приветственное письмо при регистрации**
- **Валидация форм (запрещённые слова, отрицательная цена)**
- **Стилизация форм Bootstrap**
- **Модерация продуктов:**   (новое)
  - Товары могут быть опубликованы/скрыты модератором
  - На главной странице видны только опубликованные товары
- **Владелец продукта:**     (новое) 
  - Редактирование и удаление доступно только владельцу
  - Модератор может редактировать и удалять любые товары
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
│ │  ├── load_data.py                         # Команда загрузки данных
│ │  └── create_moderator_group.py            # Создание группы модераторов
│ │
│ ├── migrations/                             # Миграции БД
│ ├── templates/                              # Шаблоны
│ │ └── catalog/
│ │  ├── base.html                            # Базовый шаблон
│ │  ├── product_detail.html                  # Страница товара
│ │  ├── home.html                            # Главная страница
│ │  ├── contacts.html                        # Контакты
│ │  ├── product_confirm_delete.html          # Подтверждение удаления
│ │  ├── product_form.html                    # Форма создания/редактирования
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
│ ├── js/
│ └── images/                                 # Изображения (фон, логотип)
│
├── users/                                    # Приложение пользователей (новое)
│ ├── migrations/                             # Миграции пользователей
│ ├── templates/users/                        # Шаблоны пользователей
│ │  ├── register.html                        # Регистрация
│ │  └── login.html                           # Вход
│ ├── admin.py                                # Регистрация модели User
│ ├── forms.py                                # Формы регистрации и входа
│ ├── models.py                               # Кастомная модель User
│ ├── urls.py                                 # Маршруты пользователей
│ └── views.py                                # Регистрация, вход, выход
│
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

Создать группу модераторов

```bash
python manage.py create_moderator_group    (новое)


Создать суперпользователя:
python manage.py createsuperuser

Назначить пользователя модератором (в shell)

from users.models import User
from django.contrib.auth.models import Group
user = User.objects.get(email='admin@example.com')
group = Group.objects.get(name='Модератор продуктов')
user.groups.add(group)


Запустить сервер:
bash
python manage.py runserver


Открыть в браузере:

Главная страница: http://127.0.0.1:8000/

Страница товара: http://127.0.0.1:8000/product/1/

Контакты: http://127.0.0.1:8000/contacts/

Блог: http://127.0.0.1:8000/blogs/

Админ-панель: http://127.0.0.1:8000/admin/

Регистрация и авторизация
Регистрация: http://127.0.0.1:8000/users/register/

Вход: http://127.0.0.1:8000/users/login/


CRUD для товаров

- Создать товар: http://127.0.0.1:8000/product/create/                                 (новое)
- Редактировать: на странице товара → "Редактировать" (только владелец или модератор)
- Удалить: на странице товара → "Удалить" (только владелец или модератор)


Лицензия
MIT License

Copyright (c) 2026 Михаил Зизганов