import pytest
import selenium
import re
from selenium.webdriver.support.ui import Select


import time

from BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.SigninPage import SigninPage
from pageObjects.SignupPage import SignupPage
from pageObjects.Signout import Signout
from pageObjects.ShowaddressPage import ShowaddressPage
from pageObjects.ResultaddressPage import ResultaddressPage
from pageObjects.DeleteaddressPage import DeleteaddressPage


from manage_data import manage_data
from manage_data import manage_data_address



@pytest.mark.usefixtures("setup")
class TestE2E(BaseClass):
    
    def test_e2e(self):
        self.driver.implicitly_wait(10)
        
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info(home_page.title())
        
        #Access Sign In Page
        sign_in = home_page.sign_in()
        log.info("{} Page".format(sign_in.title()))
        
        file_akun = "filecsv/akun.csv"
        emails = []
        passwords = []
        emails = manage_data().get_username(file_akun)
        passwords = manage_data().get_password(file_akun)
        
        #For SIGN UP if dont have account
        
        for i in range(len(emails)):
            #Access Sign Up Page
            sign_up = sign_in.sign_up()
            log.info("{} Page".format(sign_up.title()))

            log.info("email = {}".format(emails[i]))
            log.info("password = {}".format(passwords[i]))

            sign_up.email_signup(emails[i])
            sign_up.password_signup(passwords[i])
            sign_up.submit_signup()
            time.sleep(5)
            
            try :
                Signout(self.driver).signout().click()
                log.info("Successfully sign up with email = {0} and password = {1}".format(emails[i], passwords[i]))
                time.sleep(5)
            except :
                log.error("Failed Sign up with email = {0} and password = {1}".format(emails[i], passwords[i]))
                home_page.sign_in()
                
        
        #After sign up, continue to sign in
        for j in range(len(emails)):
            log.info("{} Page".format(sign_in.title()))
            
            log.info("email = {}".format(emails[j]))
            log.info("password = {}".format(passwords[j])) 
            
            sign_in.email_signin(emails[j])
            sign_in.password_signin(passwords[j])
            sign_in.submit_signin()
            
            time.sleep(3)
            
            try :
                show_address = sign_in.show_address()
                log.info("Succcessfully sign in with email = {0} and password = {1}".format(emails[j], passwords[j]))
                time.sleep(3)
                try :
                    
                    address_file = "filecsv/address.csv"
                    
                    
                    log.info("Enter the address")
                    data = manage_data_address().read_file(address_file)
                    log.debug(data["first_name"][j])
                    log.debug("get the function of manage the address")
                    #total row of data  
                    sum_row = len(data.index)
                    log.debug(sum_row)
                    log.debug(type(sum_row))
                    
                    list_id_of_input = []
                    for i in range(sum_row):
                        
                        add_address = show_address.add_address()
                        
                        log.debug(i)
                        add_address.first_name().send_keys(data['first_name'][i])
                        add_address.last_name().send_keys(data['last_name'][i])
                        add_address.address1().send_keys(data['address1'][i])
                        add_address.address2().send_keys(data['address2'][i])
                        add_address.city().send_keys(data['city'][i])
                        add_address.state().click()
                        select = Select(add_address.state())
                        select.select_by_value(data['state'][i])
                        
                        log.debug(data['zip_code'][i])
                        #state
                        add_address.zip_code().send_keys(str(data['zip_code'][i]))
                        #add_address.country
                        add_address.country(data['country'][i]).click()
                        
                        add_address.birthday().send_keys(data['birthday'][i])
                        #color
                        add_address.age().send_keys(str(data['age'][i]))
                        add_address.website().send_keys(data['website'][i])
                        #picture
                        add_address.phone().send_keys(str(data['phone'][i]))
                        
                        if str(data['interest_climb'][i]) == "1":
                            log.debug(str(data['interest_climb'][i]))
                            add_address.interest_climb().click()
                            
                            
                        if str(data['interest_dance'][i]) == "1":
                            log.debug(str(data['interest_dance'][i]))
                            add_address.interest_dance().click()
                            
                        
                        if str(data['interest_read'][i]) == "1":
                            log.debug(str(data['interest_read'][i]))
                            add_address.interest_read().click()
                            
                            
                        add_address.note().send_keys(data['note'][i])
                        
                        add_address.submit_create().click()
                        
                        log.info("Successfully add new address")
                        
                        time.sleep(3)
                        
                        log.debug("wait for the id")
                        
                        url = self.driver.current_url
                        
                        log.debug(url)
                        id_address = re.sub(".*addresses/", "", url)
                        list_id_of_input.append(id_address)
                        
                        log.info("ID Address : {}".format(id_address))
                        
                        #back to list of addresses
                        add_address.back_to_list().click()
                        #break
                        
                    #========================
                    #SHOW THE ADDRESS THAT HAS BEEN CREATED#
                    for k in range(len(list_id_of_input)):
                        ResultaddressPage(self.driver).result_address(list_id_of_input[k])
                        log.info("SHOW ADDRESS ID {}".format(list_id_of_input[k]))
                        time.sleep(2)
                        ResultaddressPage(self.driver).screenshot(list_id_of_input[k])
                        add_address.back_to_list().click()
                        
                    for d in range(len(list_id_of_input)):
                        DeleteaddressPage(self.driver).delete_address(list_id_of_input[d])
                        DeleteaddressPage(self.driver).alert_delete()
                        log.info("DELETED ADDRESSS ID {}".format(list_id_of_input[d]))
                        
                        
                        
                        
                        
                except Exception as e:
                    log.error(e)
                    log.error("Failed to add address")
                    break
                    
                    
                    #break
                
                #sign out
                Signout(self.driver).signout().click()
                log.info("SIGN OUT FROM email = {0} and password = {1}".format(emails[j], passwords[j]))
                
            except Exception as e:
                log.error(e)
                log.error("Failed Sign in with email = {0} and password = {1}".format(emails[i], passwords[i]))
                
            
    def create_address(self, data, i):
        
        #first_name = data['first_name'].tolist()
        #last_name = data['last_name'].tolist()
        #address1 = data['address1'].tolist()
        #address2 = data['address2'].tolist()
        #city = data['city'].tolist()
        #state = data['state'].tolist()
        #zip_code = data['zip_code'].tolist()
        #country = data['country'].tolist()
        #birthday = data['birthday'].tolist()
        #color = data['color'].tolist()
        #age = data['age'].tolist()
        #website = data['website'].tolist()
        #picture = data['picture'].tolist()
        #phone = data['phone'].tolist()
        #interest_climb = data['interest_climb'].tolist()
        #interest_dance = data['interest_dance'].tolist()
        #interest_read = data['interest_read'].tolist()
        #note = data['note'].tolist()
        
        #add_address = Addaddress_Page(self.driver)
        
        
        
        #add_address.first_name().send_keys(data['first_name'][i])
        #add_address.last_name().send_keys(data['last_name'][i])
        
        log.info("can be accessed")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
        
        
        
        
        
    
