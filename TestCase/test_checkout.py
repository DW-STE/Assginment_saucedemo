from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import openpyxl
service1=Service(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
from PageObj.Loginpage import Login
from Utilities.XLUtils import XLUtils
from PageObj.Cartpage import Cart
from PageObj.CheckoutPage import Checkout


class Test_checkout:
    baseurl = 'https://www.saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'
    path = "./TestData/testdata.xlsx"

    def test_checkout(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        self.obj1.cart().click()
        self.obj1.checkout().click()
        self.obj2=Checkout(self.driver)
        for r in range(2, 8):
            self.firstname = XLUtils.readData(self.path, "Sheet2", r, 1)
            self.lastname = XLUtils.readData(self.path, "Sheet2", r, 2)
            self.pin = XLUtils.readData(self.path, "Sheet2", r, 3)
            self.exp = XLUtils.readData(self.path, "Sheet2", r, 4)
            self.obj2.first_name().send_keys(self.firstname)
            self.obj2.last_name().send_keys(self.lastname)
            self.obj2.pincode().send_keys(self.pin)
            self.obj2.continuebutton_checkout().click()
            self.driver.implicitly_wait(10)
            check_overview_title=self.obj2.checkoutoverview_title()
            act_title = check_overview_title.text
            exp_title = 'Checkout: Overview'

            if act_title == exp_title:
                if self.exp == "pass":
                    print("***** Passed")

                elif self.exp == "fail":
                    print("***** Failed")

            elif act_title != exp_title:
                if self.exp == "pass":
                    print("***** failed")

                elif self.exp == "fail":
                    print("***** Passed")


    def test_checkout_cancel(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        self.obj1.cart().click()
        self.obj1.checkout().click()
        self.obj2 = Checkout(self.driver)
        self.obj2.first_name().send_keys('a')
        self.obj2.last_name().send_keys('a')
        self.obj2.pincode().send_keys('a')
        self.obj2.cancel_check().click()
        self.driver.implicitly_wait(10)
        try:
            self.obj1.yourcart_title()
            print('present')
            assert True
        except :
            print('page not redirected to your cart')
            assert False

    def test_finish_btn(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        self.obj1.cart().click()
        self.obj1.checkout().click()
        self.obj2 = Checkout(self.driver)
        self.obj2.first_name().send_keys('a')
        self.obj2.last_name().send_keys('a')
        self.obj2.pincode().send_keys('a')
        self.obj2.continuebutton_checkout().click()
        self.obj2.finish().click()
        self.driver.implicitly_wait(10)
        try:
            self.obj2.order_complete()
            print('Order placed')
            assert True
        except:
            print('Order failed')
            assert False

    def test_cancelbtn_prod(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        self.obj1.cart().click()
        self.obj1.checkout().click()
        self.obj2 = Checkout(self.driver)
        self.obj2.first_name().send_keys('a')
        self.obj2.last_name().send_keys('a')
        self.obj2.pincode().send_keys('a')
        self.obj2.continuebutton_checkout().click()
        self.obj2.cancelorder().click()
        self.driver.implicitly_wait(10)
        try:
            self.obj1.product_title()
            print('Back to products')
            assert True
        except:
            print('Failed to go back')
            assert False