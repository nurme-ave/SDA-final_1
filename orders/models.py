import datetime

from django.db import models

from store.models import Product
from accounts.models import Profile


class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        ("NP", "Not Paid"),
        ("PD", "Paid"),
        ("SH", "Shipped"),
    )

    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(default=datetime.date.today)
    active_basket = models.BooleanField()
    invoice_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    order_status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default='NP')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'OrderID: {self.pk} - User: {self.client}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order} - {self.product} - {self.quantity}pcs'
