from selenium.webdriver.common.by import By

from pageObjects.SigninPage import SigninPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    
    def title(self):
        title = self.driver.find_element_by_css_selector('[class="container"] [class="text-center"] h1').text
        return title
    
    def sign_in(self):
        sign_in = self.driver.find_element_by_id("sign-in").click()
        signin_page = SigninPage(self.driver)
        return signin_page
