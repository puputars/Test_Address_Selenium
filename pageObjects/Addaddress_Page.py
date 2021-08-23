class Addaddress_Page:
    def __init__(self, driver):
        self.driver = driver
        
    def first_name(self):
        return self.driver.find_element_by_name("address[first_name]")
    
    def last_name(self):
        return self.driver.find_element_by_name("address[last_name]")
        
    def address1(self):
        return self.driver.find_element_by_name("address[address1]")
    
    def address2(self):
        return self.driver.find_element_by_name("address[address2]")
    
    def city(self):
        return self.driver.find_element_by_name("address[city]")
    
    def state(self):
        return self.driver.find_element_by_name("address[state]")
    
    def zip_code(self):
        return self.driver.find_element_by_name("address[zip_code]")
    
    #country
    
    def country(self, country):
        if country == "us":
            return self.driver.find_element_by_id("address_country_us")
        elif country == "canada":
            return self.driver.find_element_by_id("address_country_canada")

    
    def birthday(self):
        return self.driver.find_element_by_name("address[birthday]")

    #def color
    
    def age(self):
        return self.driver.find_element_by_name("address[age]")
    
    def website(self):
        return self.driver.find_element_by_name("address[website]")
    
    
    #picture
    
    def phone(self):
        return self.driver.find_element_by_name("address[phone]")
    
    def interest_climb(self):
        return self.driver.find_element_by_id("address_interest_climb")
    
    def interest_dance(self):
        return self.driver.find_element_by_id("address_interest_dance")
    
    def interest_read(self):
        return self.driver.find_element_by_id("address_interest_read")
    
    def note(self):
        return self.driver.find_element_by_name("address[note]")
    
    def submit_create(self):
        return self.driver.find_element_by_css_selector("[data-test='submit']")
    
    
    def back_to_list(self):
        return self.driver.find_element_by_css_selector("[data-test='list']")
    
    