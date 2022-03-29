from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Returns a webdriver."""

    # stop the browser from opening
    options = Options()
    options.headless = True
    # creating the driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver


def get_page_source(driver, url):
    """Returns the HTML code of the page."""

    try:
        driver.get(url)
        html = driver.page_source
        driver.close()
        return html
    except Exception as e:
        print(f"Error: {e}")
        return None
