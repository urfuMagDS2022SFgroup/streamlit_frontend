import pytest
from playwright.sync_api import Page

from tests.files.constants import CONNECTION_URL, CONNECTION_PORT


@pytest.fixture(scope="function", autouse=True)
def main_page(page: Page) -> Page:
    page.goto(f"{CONNECTION_URL}:{CONNECTION_PORT}")
    yield
