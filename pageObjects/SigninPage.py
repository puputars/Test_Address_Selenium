from pageObjects.SignupPage import SignupPage
from pageObjects.ShowaddressPage import ShowaddressPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

import time

class SigninPage:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)
        wait.until(ES.presence_of_element_located((By.CSS_SELECTOR, ".container")))
        
    def sign_up(self):
        sign_up = self.driver.find_element_by_css_selector("[data-test='sign-up']").click()
        time.sleep(3)
        signup_page = SignupPage(self.driver)
        return signup_page
    
    def title(self):
        title = self.driver.find_element_by_css_selector(".container #clearance h2").text
        return title
        
    def email_signin(self, email):
        return self.driver.find_element_by_name("session[email]").send_keys(email)
    
    def password_signin(self, password):
        return self.driver.find_element_by_name("session[password]").send_keys(password)
        
        
    def submit_signin(self):
        return self.driver.find_element_by_css_selector("[data-disable-with='Sign in']").click()
        
    def show_address(self):
        self.driver.find_element_by_css_selector("[data-test='addresses']").click()
        time.sleep(3)
        showaddress_page = ShowaddressPage(self.driver)
        return showaddress_page