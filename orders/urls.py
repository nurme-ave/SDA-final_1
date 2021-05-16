from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order_placed/', views.order_placed, name='order_placed'),
]
