from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .forms import ProductForm
from .models import Product, Category


@method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        messages.success(request, f"Спасибо, {name}! Телефон: {phone}. Сообщение: {message}")
        return render(request, self.template_name)


# CRUD для продуктов
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.can_unpublish_product')


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.has_perm('catalog.delete_product')


# Низкоуровневое кеширование для категорий
class CategoriesListView(ListView):
    model = Category
    template_name = "catalog/categories_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        queryset = cache.get('all_categories')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('all_categories', queryset, 60 * 15)
        return queryset