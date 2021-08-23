
import selenium
from selenium import webdriver
import re, pytest, time
from BaseClass import BaseClass


class test_coba():
    def test_me(self):
        driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
        driver.get("http://a.testaddressbook.com/")
        time.sleep(5)
        url = driver.current_url
        print(url)
        
if __name__ == "__main__":
    test_coba().test_me()