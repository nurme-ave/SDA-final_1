from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)    # grab the session data
    if request.POST.get('action') == 'post':    # if the request received from the AJAX is a post request and action == post
        product_id = int(request.POST.get('productid'))     # collect the product id
        product_qty = int(request.POST.get('productqty'))   # collect the product quantity
        product = get_object_or_404(Product, id=product_id)     # get the product from the database by id
        basket.add(product=product, qty=product_qty)    # send/save the product data and quantity data into the session

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'total': baskettotal})     # send back the new updated basket quantity to the user
        return response
