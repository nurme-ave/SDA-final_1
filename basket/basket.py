
class Basket:
    """A base Basket class."""
    def __init__(self, request):
        self.session = request.session

        # first of all, we need to check if the user already has a session/cookie or not
        # if the user has a session we get the key and store that key in the variable 'basket'
        basket = self.session.get('session_key')

        # if the user does not have a session we will need to build one for the user
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {'number': 1231231}

        # return the data of the session and store it in self.basket to make the variable available
        self.basket = basket
