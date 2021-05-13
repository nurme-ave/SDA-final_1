from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class MySignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy("store:all_products")
