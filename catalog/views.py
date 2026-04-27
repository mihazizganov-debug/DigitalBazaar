from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Product


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', 'Гость')
        phone = request.POST.get('phone', 'не указан')
        message = request.POST.get('message', 'пустое сообщение')
        messages.success(
            request,
            f'Спасибо, {name}! Сообщение "{message}" отправлено. Мы позвоним по номеру {phone}.'
        )
        return render(request, self.template_name)
