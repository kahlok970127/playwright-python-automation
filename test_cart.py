from auth import Auth_action
from inventory import inventory_action
from shopingcart import Cart_action


def test_product_show_in_cart(page):

    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")

    inventory = inventory_action(page)
    inventory.add_multiple_product(2)

    cart = Cart_action(page)
    cart.open_cart()

    assert cart.cart_items.count() == 2