from playwright.sync_api import expect

def test_product_show_in_cart(inventory_page,cart_page):
    inventory_page.add_multiple_product(2)
    cart_page.open_cart()
    assert cart_page.cart_items.count() == 2


def test_cart_innertext_count(inventory_page, cart_page):
    inventory_page.add_multiple_product(3)
    assert cart_page.shopping_cart_badge.inner_text() == "3"


def test_certain_product_name_match_in_cart(inventory_page, cart_page):
    inventory_page.add_certain_item('Sauce Labs Bike Light')
    cart_page.open_cart()
    assert cart_page.inventory_item_name.inner_text() == 'Sauce Labs Bike Light'


def test_added_item_match_in_cart(inventory_page, cart_page):

    inventory_price = inventory_page.get_product_price('Sauce Labs Bike Light')
    inventory_page.add_certain_item('Sauce Labs Bike Light')
    cart_page.open_cart()
    assert cart_page.inventory_item_price.inner_text() == inventory_price

def remove_product(inventory_page, cart_page):
    inventory_page.add_certain_item('Sauce Labs Bike Light')
    cart_page.open_cart()
    cart_page.remove_certain_product('Sauce Labs Bike Light')
    expect(cart_page.shopping_cart_badge).to_have_count(0)

def test_checkout_button(cart_page):

    cart_page.open_cart()
    cart_page.checkout_cart()
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")