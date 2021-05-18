from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView

from accounts.forms import SignUpForm
from accounts.models import Profile
from orders.models import Order, OrderItem

from basket.basket import Basket

from store.models import Product


class MySignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")


class CustomerLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        result = super().form_valid(form)

        user = self.request.user
        profile = Profile.objects.get(user=user)
        my_basket = Basket(self.request)  # this is the offline basket (before logging in)

        if Order.objects.filter(client=profile, active_basket=True).exists():
            active_order = Order.objects.get(client=profile, active_basket=True)
        else:
            if len(my_basket) > 0:
                active_order = Order.objects.create(
                    client=profile,
                    active_basket=True,
                )
            else:
                return result

        order_items = active_order.items.all()

        my_basket_copy = {}
        for key in my_basket.basket:
            my_basket_copy[key] = my_basket.basket[key].copy()

        for item in order_items:    # update the session basket from the database
            my_basket.add(item.product, item.quantity)

        for product_id in my_basket_copy:   # update the database with the copy of the offline basket
            my_product = Product.objects.get(id=int(product_id))
            if OrderItem.objects.filter(product=my_product, order=active_order).exists():
                item = OrderItem.objects.get(product=my_product, order=active_order)
                item.quantity += my_basket_copy[product_id]['qty']
                item.save()
            else:
                OrderItem.objects.create(
                    order=active_order,
                    product=my_product,
                    price=my_product.price,
                    quantity=my_basket_copy[product_id]['qty']
                )

        return result


class CustomerPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_success')


def customer_password_change_success(request):
    return render(request, 'accounts/password_change_success.html')


def customer_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def order_history(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    completed_orders = Order.objects.filter(client=profile, active_basket=False).order_by('-id')

    # for order in completed_orders:
    #     items = OrderItem.objects.filter(order=order.pk)
    #     for item in items:
    #         print(f'{order.pk} - {item.product} - {item.quantity}pcs - €{item.product.price}')

    return render(request, 'accounts/order_history.html', {'orders': completed_orders})
