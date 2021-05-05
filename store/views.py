from django.shortcuts import render
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all().order_by('name')
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
