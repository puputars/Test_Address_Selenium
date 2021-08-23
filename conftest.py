import pytest
from selenium import webdriver
import time
driver = None



@pytest.fixture(scope="class")
def setup(request):
    global driver

    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    driver.get("http://a.testaddressbook.com/")
    driver.maximize_window()

    request.cls.driver = driver
    #yield
    #driver.close()