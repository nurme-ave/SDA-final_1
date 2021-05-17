from .models import OrderItem
from store.models import Product


def add_item_to_order(active_order, product_id, product_qty):
    """Add the item to the database."""
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


def remove_item_from_order(active_order, product_id):
    """Remove the item from the database."""
    order_item = OrderItem.objects.get(order=active_order, product=product_id)
    order_item.delete()


def update_item_in_order(active_order, product_id, product_qty):
    """Update the item's quantity in the database."""
    order_item = OrderItem.objects.get(order=active_order, product=product_id)
    order_item.quantity = product_qty
    order_item.save()
