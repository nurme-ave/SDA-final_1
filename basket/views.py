from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

import orders.orders
from accounts.models import Profile
from orders.models import Order

from store.models import Product
from .basket import Basket
from orders.orders import *


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_action(request):
    user = request.user
    # orderID = Order.pk

    active_order = None
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        if Order.objects.filter(client=profile, active_basket=True).exists():
            active_order = Order.objects.get(client=profile, active_basket=True)
        else:
            active_order = Order.objects.create(
                client=profile,
                active_basket=True,
            )

    basket = Basket(request)  # grab the session data

    if request.POST.get(
            'action') == 'add':  # if the request received from the AJAX is a post request and action == post
        product_id = int(request.POST.get('productid'))  # collect the product id
        product_qty = int(request.POST.get('productqty'))  # collect the product quantity
        product_data = get_object_or_404(Product, id=product_id)  # get the product from the database by id
        basket.add(product_data=product_data,
                   qty=product_qty)  # send/save the product data and quantity data into the session

        if active_order:
            add_item_to_order(active_order, product_id, product_qty)

    elif request.POST.get('action') == 'delete':
        product_id = int(request.POST.get('productid'))
        basket.update_quantity_or_remove_item(product_id=product_id)

        # if active_order:
        #     remove_item_from_order(active_order, product_id)

    elif request.POST.get('action') == 'update':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update_quantity_or_remove_item(product_id=product_id, qty=product_qty, update=True)
        #
        # if active_order:
        #     update_item_in_order(active_order, product_id)

    basket_qty = basket.__len__()
    basket_total = basket.get_total_price()
    response = JsonResponse(
        {'qty': basket_qty, 'total': basket_total})  # send back the new updated basket quantity to the user
    return response
