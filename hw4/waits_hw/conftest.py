import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# в внешнем conftest лежит основная логика
@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    options.add_argument('--headless')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver) -> WebDriverWait:
    wait = WebDriverWait(driver, timeout=15)
    return wait
