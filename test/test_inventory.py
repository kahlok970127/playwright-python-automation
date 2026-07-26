from playwright.sync_api import expect
from page.login import Auth_action
from page.inventory import inventory_action
from page.shopping_cart import Cart_action

def test_item_not_empty(inventory_page):
    assert inventory_page.products.count() > 0


def test_check_add_to_cart_button(inventory_page):
    assert inventory_page.addtocart.count() > 0

def test_add_product_to_cart(inventory_page):
    inventory_page.add_single_product()
    assert inventory_page.badge.inner_text() == "1"

def test_add_multiple_product_to_cart(inventory_page):
    inventory_page.add_multiple_product(3)
    assert inventory_page.badge.inner_text() == "3"


def test_remove_product_to_cart(inventory_page):
    inventory_page.add_single_product()
    inventory_page.remove_single_product()
    expect(inventory_page.badge).to_have_count(0)


def test_remove_multiple_product_to_cart(inventory_page):
    inventory_page.add_multiple_product(3)
    inventory_page.remove_multiple_product(2)
    assert inventory_page.badge.inner_text() == "1"


def test_product_price_not_empty(inventory_page):
    assert inventory_page.prices.count() > 0


def test_every_product_image_loaded(inventory_page):
    assert inventory_page.products.count() == inventory_page.images.count()

    for i in range(inventory_page.images.count()):
        img = inventory_page.images.nth(i)
        expect(img).to_be_visible()
        assert img.evaluate("(img) => img.complete && img.naturalWidth > 0")


def test_sort_low_to_high(inventory_page):
    inventory_page.sort_low_to_high()
    prices = inventory_page.get_prices()
    assert prices == sorted(prices)


def test_sort__high_to_low(inventory_page):
    inventory_page.sort_high_to_low()
    prices = inventory_page.get_prices()
    assert prices == sorted(prices,reverse=True)

def test_sort_name_asc(inventory_page):

    inventory_page.sort_name_asc()
    names = inventory_page.get_names()
    assert names == sorted(names)

def test_sort_name_desc(inventory_page):

    inventory_page.sort_name_desc()
    names = inventory_page.get_names()
    assert names == sorted(names, reverse=True)

