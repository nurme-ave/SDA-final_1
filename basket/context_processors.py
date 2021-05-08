"""
Make the basket available globally across all templates.
P.S. -> Don't forget to specify the context processor in the settings file.
"""

from .basket import Basket


def basket(request):
    """The data returned here is the default data that gets initialized in the Basket."""
    return {'basket': Basket(request)}
