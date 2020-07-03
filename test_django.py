import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_basic():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            yield driver
    else:
        with webdriver.Chrome() as driver:
            yield driver

    driver.get('http://127.0.0.1:8000/')
    assert 'Hello, world!' in driver.page_source
    driver.close()
