from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_action(request):
    basket = Basket(request)    # grab the session data

    if request.POST.get('action') == 'add':    # if the request received from the AJAX is a post request and action == post
        product_id = int(request.POST.get('productid'))     # collect the product id
        product_qty = int(request.POST.get('productqty'))   # collect the product quantity
        product = get_object_or_404(Product, id=product_id)     # get the product from the database by id
        basket.add(product=product, qty=product_qty)    # send/save the product data and quantity data into the session

    elif request.POST.get('action') == 'delete':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

    elif request.POST.get('action') == 'update':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

    basket_qty = basket.__len__()
    basket_total = basket.get_total_price()
    response = JsonResponse({'qty': basket_qty, 'total': basket_total})     # send back the new updated basket quantity to the user
    return response
