from decimal import Decimal

from django.shortcuts import render

from accounts.models import Profile
from basket.basket import Basket
from .models import Order


def order_placed(request):
    basket = Basket(request)
    user = request.user
    profile = Profile.objects.get(user=user)
    active_order = Order.objects.get(client=profile, active_basket=True)

    print(active_order.active_basket)
    print(active_order.order_status)

    active_order.active_basket = False
    active_order.order_status = 'PD'
    active_order.invoice_total = Decimal(basket.get_total_price())

    print(active_order.active_basket)
    print(active_order.order_status)
    print(active_order.invoice_total)

    active_order.save()
    basket.clear()

    return render(request, 'orders/order_placed.html')
