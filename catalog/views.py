from django.shortcuts import render
from django.contrib import messages  # 👈 добавить эту строку


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':  # 👈 проверяем, отправили ли форму
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Пока просто показываем сообщение (отправка email по желанию)
        messages.success(request, f'Спасибо, {name}! Ваше сообщение отправлено.')

        return render(request, 'catalog/contacts.html')

    return render(request, 'catalog/contacts.html')