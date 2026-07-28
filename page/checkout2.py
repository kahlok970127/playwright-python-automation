class Checkout_action2():
    def __init__(self,page):
        self.page = page

        self.finish_button = page.locator("#finish")       
        self.back_home_button = page.locator("#back-to-products")
        self.generate_report = page.locator("#generate-pdf-order")



    def click_finish_button(self):
        self.finish_button.click()

    def generate_reporrt(self):
        self.generate_report.click()

    def back_home(self):
        self.back_home_button.click()




