"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('item/<slug:slug>/', views.product_detail, name="product_detail"),
    path('shop/<slug:category_slug>/', views.category_list, name="category_list"),
    path('search_in_products/', views.search_in_products, name='search_in_products'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('personalized_offers', views.personalized_offers, name='personalized_offers')
]
