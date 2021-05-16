from django.shortcuts import render

from basket.basket import Basket


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'orders/order_placed.html')
