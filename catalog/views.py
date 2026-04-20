from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product

def home(request):
    products = Product.objects.all()  # 👈 получаем все товары
    return render(request, 'catalog/home.html', {'products': products})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        messages.success(request, f'Спасибо, {name}! Ваше сообщение отправлено.')
        return render(request, 'catalog/contacts.html')
    return render(request, 'catalog/contacts.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})