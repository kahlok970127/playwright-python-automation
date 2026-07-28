from playwright.sync_api import Playwright, sync_playwright,expect


def test_submit_order(cart_page,checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.last_name.fill("lastname")
    checkout_page.postal_code.fill("postal_code")
    checkout_page.click_continue_button()
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")


def test_empty_all(cart_page,checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.click_continue_button()
    expect(checkout_page.error).to_have_text("Error: First Name is required")

def test_empty_lastname_and_postal(cart_page,checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.click_continue_button()
    expect(checkout_page.error).to_have_text("Error: Last Name is required")

def test_empty_postal(cart_page,checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.last_name.fill("lastname")
    checkout_page.click_continue_button()
    expect(checkout_page.error).to_have_text("Error: Postal Code is required")

def test_cancel_checkout(cart_page,checkout_page):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.click_cancel_button()
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/cart.html")


