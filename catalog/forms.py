from django import forms

from .models import Product

# Запрещённые слова (список)
FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "category":
                field.widget.attrs["class"] = "form-select"

    def _check_forbidden_words(self, value, field_name):
        """Проверка на наличие запрещённых слов"""
        if value:
            value_lower = value.lower()
            for word in FORBIDDEN_WORDS:
                if word in value_lower:
                    raise forms.ValidationError(f'Поле "{field_name}" содержит запрещённое слово: "{word}".')

    def clean_name(self):
        name = self.cleaned_data.get("name")
        self._check_forbidden_words(name, "название")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        self._check_forbidden_words(description, "описание")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price
