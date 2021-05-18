from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def all_products(request):
    products = Product.objects.filter(is_active=True, in_stock=True)
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)    # equivalent to SQL statement using the WHERE clause
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def search_in_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_products = Product.objects.filter(title__contains=searched)
        return render(request, 'store/search.html', {'searched': searched, 'search_products': search_products})
