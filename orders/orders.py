from .models import OrderItem
from store.models import Product


def add_item_to_order(active_order, product_id, product_qty):
    if OrderItem.objects.filter(order=active_order, product=product_id).exists():
        order_item = OrderItem.objects.get(
            order=active_order,
            product=Product.objects.get(id=product_id)
        )
        order_item.quantity += product_qty
        order_item.save()

    else:
        OrderItem.objects.create(
            order=active_order,
            product=Product.objects.get(id=product_id),
            quantity=product_qty,
            price=Product.objects.get(id=product_id).price
        )


    items = active_order.items.all()
    for item in items:
        print(f'{item.product} - {item.quantity}')

    print(f'ID: {product_id} - {product_qty}pcs')


def remove_item_from_order(order, orderitem):
    pass


def update_item_in_order(order, orderitem):
    pass
