from decimal import Decimal

from store.models import Product


class Basket:
    """A base Basket class."""

    def __init__(self, request):
        self.session = request.session

        # first of all, we need to check if the user already has a session/cookie or not
        # if the user has a session we get the key and store that key in the variable 'basket'
        basket = self.session.get('session_key')

        # if the user does not have a session we will need to build one for the user
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}

        # return the data of the session and store it in self.basket to make the variable available
        self.basket = basket

    def save(self):
        """Tell Django explicitly that the session has been modified."""
        self.session.modified = True

    def add(self, product, qty):
        """Adding and updating the users basket session data."""
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        else:
            self.basket[product_id]['qty'] += int(qty)

        self.save()

    def update_quantity_or_remove_item(self, product, qty=None, update=None):
        """
        Update values in session data or remove an item from the basket based on the
        'update' argument which is passed in from views.basket_action.
        """
        product_id = str(product)

        if product_id in self.basket and update:
            self.basket[product_id]['qty'] = qty
        else:
            del self.basket[product_id]

        self.save()

    def __iter__(self):
        """Collect the product_id in the session data to query the database and return products."""
        product_ids = self.basket.keys()  # iterate over the keys in the basket and collect them
        products = Product.objects.filter(id__in=product_ids)  # collect items which id's are in the session data
        basket = self.basket.copy()  # make a copy of the session data

        for product in products:
            basket[str(product.id)][
                'product'] = product  # add additional data to our basket, in this case all the product data

        for item in basket.values():
            item['price'] = Decimal(
                item['price'])  # convert the price from a string into a decimal otherwise we can't make the calculation
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """Get the basket data and count the qty of items."""
        return sum(item['qty'] for item in self.basket.values())  # iterate through the basket and add quantities up

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
