from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import SignUpForm
from accounts.models import Profile


class MySignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")


class CustomerLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomerPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_success')


def customer_password_change_success(request):
    return render(request, 'accounts/password_change_success.html')


class CustomerProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = Profile
