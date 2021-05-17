
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.db.transaction import atomic

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'country']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))
    country = CountryField(blank_label='Select country from the list...').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'}))

    @atomic
    def save(self, commit=True):
        # self.instance.is_active = False
        result = super().save(commit)
        phone = self.cleaned_data['phone']
        country = self.cleaned_data['country']
        profile = Profile(phone=phone, country=country, user=result)

        if commit:
            profile.save()
        return result
