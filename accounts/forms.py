from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from accounts.models import Profile


class MySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(label='Biography', widget=Textarea(attrs={'placeholder': 'Tell us your story with movies'}),
                          min_length=40)
