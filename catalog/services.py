from django.core.cache import cache

from .models import Product


def get_products_by_category(category_id):
    """Возвращает список продуктов в категории с кешированием"""
    cache_key = f"category_{category_id}_products"
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(category_id=category_id, is_published=True)
        cache.set(cache_key, products, 60 * 15)  # 15 минут
        print(f"Данные загружены из БД для категории {category_id}")  # для проверки
    else:
        print(f"Данные взяты из Redis для категории {category_id}")  # для проверки

    return products
