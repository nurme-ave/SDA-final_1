from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class MySignUpView(CreateView):
    template_name = 'accounts/form.html'
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")


class MyLoginView(LoginView):
    template_name = 'accounts/form.html'