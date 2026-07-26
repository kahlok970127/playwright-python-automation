from auth import Auth_action
from inventory import inventory_action



def test_item_not_empty(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")
    inventory = inventory_action(page)
    assert inventory.products.count() > 0

def test_check_add_to_cart_button(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")
    inventory = inventory_action(page)
    assert inventory.addtocart.count() > 0

def test_add_product_to_cart(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")

    inventory = inventory_action(page)
    inventory.add_single_product()

    assert inventory.badge.inner_text() == "1"

def test_multiple_product_to_cart(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")

    inventory = inventory_action(page)
    inventory.add_multiple_product(3)

    assert inventory.badge.inner_text() == "3"


