from selenium import webdriver
from selenium.webdriver.common.by import By


class Checkout:
    checkout_redirected_xpath = '//*[@id="header_container"]/div[2]/span'
    first_name_id='first-name'
    last_name_id='last-name'
    pincode_id='postal-code'
    cancel_button_urcart_id='cancel'
    continue_button_checkout='continue'
    checkout_overview_CSS='#header_container > div.header_secondary_container > span'
    finish_button_id='finish'
    cancel_button_productpageredir_id='cancel'
    checkout_complete_xpath='//*[@id="header_container"]/div[2]/span'
    back_home_id='back-to-products'                                       #loginpg


    def __init__(self, driver):
        self.driver = driver

    def first_name(self):
       return self.driver.find_element(By.ID,self.first_name_id)

    def last_name(self):
       return self.driver.find_element(By.ID, self.last_name_id)

    def pincode(self):
        return self.driver.find_element(By.ID, self.pincode_id)

    def continuebutton_checkout(self):
        return self.driver.find_element(By.ID, self. continue_button_checkout)

    def cancel_check(self):
        return self.driver.find_element(By.ID, self.cancel_button_urcart_id)

    def finish(self):
        return self.driver.find_element(By.ID, self.finish_button_id)

    def cancelorder(self):
        return self.driver.find_element(By.ID, self.cancel_button_productpageredir_id)

    def checkoutoverview_title(self):
         return self.driver.find_element(By.CSS_SELECTOR, self.checkout_overview_CSS)

    def order_complete(self):
        return self.driver.find_element(By.XPATH, self.checkout_complete_xpath)