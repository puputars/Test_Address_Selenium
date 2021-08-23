
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)
        wait.until(ES.presence_of_element_located((By.CSS_SELECTOR, ".container")))
        
    def title(self):
        #return title
        return self.driver.find_element_by_css_selector(".container #clearance h2").text
    
    def email_signup(self, email):
        return self.driver.find_element_by_name("user[email]").send_keys(email)
    
    def password_signup(self, password):
        return self.driver.find_element_by_name("user[password]").send_keys(password)
        
        
    def submit_signup(self):
        return self.driver.find_element_by_css_selector("[data-disable-with='Sign up']").click()
        