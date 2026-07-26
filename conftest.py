import pytest
from page.login import Auth_action
from page.inventory import inventory_action
import time

@pytest.fixture
def inventory_page(page):

    auth = Auth_action(page)
    auth.login("standard_user","secret_sauce")

    return inventory_action(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.test_failed = report.failed


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):

    yield

    if getattr(request.node, "test_failed", False):

        page.screenshot(path=f"screenshots/{request.node.name}_{int(time.time())}.png")