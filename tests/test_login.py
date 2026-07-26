from page.login import Auth_action


def test_login_success(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")
    auth.verify_login_success()

def test_login_success_with_enter(page):
    auth = Auth_action(page)
    auth.login_with_enter("standard_user","secret_sauce")
    auth.verify_login_success()

def test_invalid_username(page):
    auth = Auth_action(page)
    auth.login("invaliduser","secret_sauce")
    auth.verify_login_failed()

def test_invalid_password(page):
    auth = Auth_action(page)
    auth.login("standard_user","inavalid_sauce")
    auth.verify_login_failed()


def test_empty_username(page):
    auth = Auth_action(page)
    auth.login("","secret_sauce")
    auth.verify_login_failed()


def test_empty_password(page):
    auth = Auth_action(page)
    auth.login("standard_user","")
    auth.verify_login_failed()

def test_lockout_user(page):
    auth = Auth_action(page)
    auth.login("locked_out_user","secret_sauce")
    auth.verify_login_failed()

def test_both_empty(page):
    auth = Auth_action(page)
    auth.login("", "")
    auth.verify_login_failed()

def test_both_invalid(page):
    auth = Auth_action(page)
    auth.login("invalid_user", "invalid_password")
    auth.verify_login_failed()

def test_username_case_sensitive(page):
    auth = Auth_action(page)
    auth.login("Standard_User", "secret_sauce")
    auth.verify_login_failed()

def test_password_case_sensitive(page):
    auth = Auth_action(page)
    auth.login("standard_user", "Secret_Sauce")
    auth.verify_login_failed()

def test_username_spaces(page):
    auth = Auth_action(page)
    auth.login(" standard_user ", "secret_sauce")
    auth.verify_login_failed()

