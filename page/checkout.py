class Checkout_action():
    def __init__(self,page):
        self.page = page

        self.first_name = page.locator("#first-name")       
        self.last_name = page.locator("#last-name")       
        self.postal_code = page.locator("#postal-code")       
        self.continue_button = page.locator("#continue")       
        self.cancel_button = page.locator("#cancel")
        self.error = page.locator("[data-test=\"error\"]")

    def click_continue_button(self):
        self.continue_button.click()

    def click_cancel_button(self):
         self.cancel_button.click()

