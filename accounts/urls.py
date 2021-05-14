from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import MySignUpView, CustomerPasswordChangeView, CustomerProfileView, CustomerLoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', MySignUpView.as_view(), name='signup'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', CustomerPasswordChangeView.as_view(), name='password_change'),
    path('password_change_success/', views.customer_password_change_success, name='password_change_success'),
    path('customer_detail/<pk>/', CustomerProfileView.as_view(), name='customer_detail'),
]
