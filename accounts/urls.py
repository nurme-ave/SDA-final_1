from django.urls import path
from .views import MyLoginView, MySignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', MySignUpView.as_view(), name='signup'),
]