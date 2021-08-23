class Signout:
    def __init__(self, driver):
        self.driver = driver
    
    def signout(self):
        return self.driver.find_element_by_css_selector("[data-test='sign-out']")