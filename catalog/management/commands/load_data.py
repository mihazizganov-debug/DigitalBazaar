from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Загружает тестовые данные из фикстур"

    def handle(self, *args, **kwargs):
        # Очищаем существующие данные
        self.stdout.write("Очистка базы данных...")
        call_command("flush", "--noinput")

        # Загружаем фикстуры
        self.stdout.write("Загрузка категорий...")
        call_command("loaddata", "catalog/fixtures/categories.json")

        self.stdout.write("Загрузка продуктов...")
        call_command("loaddata", "catalog/fixtures/products.json")

        self.stdout.write(self.style.SUCCESS("✅ Данные успешно загружены!"))
