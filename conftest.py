import pytest
from login import Auth_action
from inventory import inventory_action


@pytest.fixture
def inventory_page(page):

    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")

    return inventory_action(page)