from playwright.sync_api import Playwright, sync_playwright,expect
import time

class inventory_action():
    def __init__(self,page):
        self.page = page
        self.inventory_item = page.locator(".inventory_item")
        self.addtocart = page.locator("[data-test^=\"add-to-cart\"]")
        self.badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.removeitem = page.locator("[data-test^=\"remove\"]")
        self.prices = page.locator("[data-test^=\"inventory-item-price\"]")
        self.images = page.locator("img.inventory_item_img")
        self.sortbutton = page.locator("[data-test^=\"product-sort-container\"]")
        self.inventory_item_name = page.locator(".inventory_item_name")
        self.addcertainitem = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")

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

    def sort_low_to_high(self):
            self.sortbutton.select_option("lohi")

    def sort_high_to_low(self):
            self.sortbutton.select_option("hilo")

    def sort_name_asc(self):
        self.sortbutton.select_option("az")

    def sort_name_desc(self):
        self.sortbutton.select_option("za")

    def get_prices(self):

        prices = []

        for i in range(self.prices.count()):
            price = self.prices.nth(i).inner_text()
            prices.append(float(price.replace("$","")))

        return prices
    
    def get_names(self):

        inventory_item_name = []
        for i in range(self.inventory_item_name.count()):
            name  = self.inventory_item_name.nth(i).inner_text()
            inventory_item_name.append(name)

        return inventory_item_name

    def add_certain_item(self, product_name):
        item = self.inventory_item.filter(has=self.inventory_item_name.filter(has_text=product_name))
        item.locator("button").click()


    def add_certain_item(self, product_name):
        item = self.inventory_item.filter(has=self.inventory_item_name.filter(has_text=product_name))
        item.locator("button").click()


    def get_product_price(self, product_name):
        item = self.inventory_item.filter(has=self.inventory_item_name.filter(has_text=product_name))
        return item.locator(".inventory_item_price").inner_text()
    
    