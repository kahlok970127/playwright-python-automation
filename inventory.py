from playwright.sync_api import Playwright, sync_playwright,expect
import time

class inventory_action():
    def __init__(self,page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.addtocart = page.locator("[data-test^=\"add-to-cart\"]")
        self.badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.removeitem = page.locator("[data-test^=\"remove\"]")

    def add_single_product(self):
        self.addtocart.first.click()

    def add_multiple_product(self, amount):
        for i in range(amount):
            self.addtocart.first.click()

    def remove_single_product(self):
        self.removeitem.first.click()

    def remove_multiple_product(self, amount):
        for i in range(amount):
            self.removeitem.first.click()


    


    