from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import UserLoginForm, UserRegisterForm
from .models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject="Добро пожаловать!",
            message=f"Здравствуйте, {self.object.email}! Вы успешно зарегистрировались на DigitalBazaar.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
            fail_silently=True,
        )
        return response


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    next_page = reverse_lazy("catalog:home")
