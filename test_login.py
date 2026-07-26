from auth import Auth_action

def test_login_success(page):
    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")
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

