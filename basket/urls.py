from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('action/', views.basket_action, name='basket_action'),
]
