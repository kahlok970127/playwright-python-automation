from playwright.sync_api import Playwright, sync_playwright,expect
import time

class Cart_action:

    def __init__(self,page):
        self.page = page
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.cart_items = page.locator(".cart_item")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.inventory_item_name = page.locator(".inventory_item_name")
        self.inventory_item_price = page.locator(".inventory_item_price")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")


    def open_cart(self):
        self.cart_button.click()

    def remove_certain_product(self,product_name):
        if isinstance(product_name, str):
            product_name = [product_name]
            # item = self.cart_items.filter(has=self.inventory_item_name.filter(has_text=product_name))
            # item.locator("button").click()

        for name in product_name:
            item = self.cart_items.filter(has=self.inventory_item_name.filter(has_text=name))
            item.locator("button").click()

    def checkout_cart(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()




    