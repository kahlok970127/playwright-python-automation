from playwright.sync_api import Playwright, sync_playwright,expect
import time

class Auth_action():
    def __init__(self,page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.loginbutton = page.locator("[data-test=\"login-button\"]")
        self.error = page.locator("[data-test='error']")
        


    def login(self,username,password):
            self.page.goto("https://www.saucedemo.com/")
            self.username.wait_for(state="visible",timeout=2000)
            self.username.click()
            self.username.fill(username)
            self.password.click()
            self.password.fill(password)
            self.loginbutton.click()


    def verify_login_success(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )


    def verify_login_failed(self):
        expect(self.error).to_be_visible()

# def run(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)

#     context = browser.new_context()
#     page = context.new_page()

#     auth = Auth_action(page)

    # login success
    # auth.login("standard_user","secret_sauce")
    
    # invalid username
    # auth.login("inavliduser","secret_sauce")

    # invalid password
    # auth.login("standard_user","inavlidpassword")

    # Empty Username
    # auth.login("","secret_sauce")

    # Empty Password
    # auth.login("standard_user","")

    # Locked Out User
    # auth.login("locked_out_user","secret_sauce")

#     context.close()
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)


# print("OK")