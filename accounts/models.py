from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=50, null=True)
    country = CountryField(null=True)

    def __str__(self):
        return str(self.user)
