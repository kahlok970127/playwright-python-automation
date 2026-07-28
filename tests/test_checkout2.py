from playwright.sync_api import Playwright, sync_playwright,expect



def test_check_out_complete(cart_page,checkout_page,checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.last_name.fill("lastname")
    checkout_page.postal_code.fill("postal_code")
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()
    expect(checkout_page2.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

def test_generate_pdf(cart_page,checkout_page,checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.last_name.fill("lastname")
    checkout_page.postal_code.fill("postal_code")   
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()
    with checkout_page2.page.expect_download() as download_info:
        checkout_page2.generate_reporrt()
    assert download_info.value is not None

def test_check_out_complete_backhome(cart_page,checkout_page,checkout_page2):
    cart_page.open_cart()
    cart_page.checkout_cart()
    checkout_page.first_name.fill("firstname")
    checkout_page.last_name.fill("lastname")
    checkout_page.postal_code.fill("postal_code")
    checkout_page.click_continue_button()
    checkout_page2.click_finish_button()
    checkout_page2.back_home()
    expect(checkout_page2.page).to_have_url("https://www.saucedemo.com/inventory.html")

