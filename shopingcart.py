from playwright.sync_api import Playwright, sync_playwright,expect
import time

class Cart_action:

    def __init__(self,page):
        self.page = page
        self.cart_button = page.locator("[data-test='shopping-cart-link']")
        self.cart_items = page.locator(".cart_item")

    def open_cart(self):
        self.cart_button.click()

    