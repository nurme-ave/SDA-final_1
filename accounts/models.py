from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, null=True)
    phone = models.CharField(max_length=50, null=True)
    country = CountryField(null=True, blank_label='Select country from the list...')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
