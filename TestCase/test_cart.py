from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service1=Service(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
from PageObj.Cartpage import Cart
from PageObj.Loginpage import Login

class Test_cart:
    baseurl = 'https://www.saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'

    def test_cart(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1=Cart(self.driver)
        self.obj1.cart().click()
        title_cart=self.obj1.yourcart_title()
        print(title_cart.text)
        if title_cart.text=='Your Cart':
            assert True
        else:
            print('page not redirected to your cart')
            self.driver.save_screenshot('.\\Screenshoots\\' + 'test_cart.png')
            assert False


    def test_cart_cont_shop_button(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.cart().click()
        self.obj1.cont_shop().click()
        prod_title=self.obj1.product_title()
        print(prod_title.text)
        print('After clicking continue shopping redirected to products')
        if prod_title.text=='Products':
            assert True
        else:
            print('Not redirecting to product page')
            self.driver.save_screenshot('.\\Screenshoots\\' + 'test_yourcart.png')
            assert False

    def test_cart_checkout_button(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.cart().click()
        self.obj1.checkout().click()
        checkout_title=self.obj1.checkout_title()
        print(checkout_title.text)
        if checkout_title.text=='Checkout: Your Information':
            print('After clicking checkout redirecting to checkout page')
            assert True
        else:
            print('Not redirecting to checkout')
            self.driver.save_screenshot('.\\Screenshoots\\' + 'checkout.png')
            assert False

    def test_add_btn(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        self.obj1.cart().click()
        assert self.obj1.prod()

    def test_remove_btn(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.addcart().click()
        time.sleep(5)
        self.obj1.cart().click()
        self.obj1.removecart().click()

        try:
            self.obj1.empty_cart()
            print('element removed')
            assert True
        except:
            print('not removed')
            self.driver.save_screenshot('.\\Screenshoots\\' + 'remove.png')
            assert False

    def test_prod_item(self):
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get(self.baseurl)
        self.obj = Login(self.driver)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        self.obj1 = Cart(self.driver)
        self.obj1.prod().click()
        self.driver.implicitly_wait(10)
        back_title=self.obj1.back_prod()
        print(back_title.text)
        if back_title.text=='Back to products':
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshoots\\' + 'products.png')
            assert False

