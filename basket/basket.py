
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

    def add(self, product, qty):
        """Adding and updating the users basket session data."""
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.session.modified = True    # tell Django we have modified the session

    def __len__(self):
        """Get the basket data and count the qty of items."""
        return sum(item['qty'] for item in self.basket.values())    # iterate through the basket and add quantities up
