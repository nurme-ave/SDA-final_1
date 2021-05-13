from django.urls import path
from .views import MyLoginView, MySignUpView


app_name = 'accounts'

urlpatterns = [
    path('signup/', MySignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
]
