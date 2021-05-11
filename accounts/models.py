from django.db.models import Model, OneToOneField, CASCADE, TextField
from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        return self.user.user_name