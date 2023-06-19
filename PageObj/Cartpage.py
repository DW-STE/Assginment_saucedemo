from selenium import webdriver
from selenium.webdriver.common.by import By


class Cart:
    product_title_CSS='#header_container > div.header_secondary_container > span'
    filter_icon_classname='product_sort_container'
    shopping_cart_id='shopping_cart_container'
    back_to_products_CSS='#back-to-products'
    prod_1_id='item_4_title_link'
    add_to_cart_id_p1 = 'add-to-cart-sauce-labs-backpack'
    remove_from_cart_id_p1= 'remove-sauce-labs-backpack'
    prod_2_id = 'item_0_title_link'
    add_to_cart_id_p2 = 'add-to-cart-sauce-labs-bike-light'
    remove_from_cart_id_p2 = 'remove-sauce-labs-bike-light'
    prod_3_id = 'item_1_title_link'
    add_to_cart_id_p3 = 'add-to-cart-sauce-labs-bolt-t-shirt'
    remove_from_cart_id_p3 = 'remove-sauce-labs-bolt-t-shirt'
    prod_4_id = 'item_5_title_link'
    add_to_cart_id_p4 = 'add-to-cart-sauce-labs-fleece-jacket'
    remove_from_cart_id_p4 = 'remove-sauce-labs-fleece-jacket'
    prod_5_id = 'item_2_title_link'
    add_to_cart_id_p5 = 'add-to-cart-sauce-labs-onesie'
    remove_from_cart_id_p5 = 'remove-sauce-labs-onesie'
    prod_6_id = 'item_3_title_link'
    add_to_cart_id_p6 = 'add-to-cart-test.allthethings()-t-shirt-(red)'
    remove_from_cart_id_p6 = 'remove-test.allthethings()-t-shirt-(red)'
    product_desc_class='inventory_details_desc large_size'
    product_price_class='inventory_details_price '
    your_cart_title_CSS='#header_container > div.header_secondary_container > span'
    cont_shop_id='continue-shopping'
    checkout_id='checkout'
    checkout_redirected_xpath='//*[@id="header_container"]/div[2]/span'
    empty_cart_class='removed_cart_item'
    checkout_ur_inf0_CSS='#header_container > div.header_secondary_container > span'


    def __init__(self, driver):
        self.driver = driver

    def cart(self):
        return self.driver.find_element(By.ID,self.shopping_cart_id)

    def filter(self):
        return self.driver.find_element(By.CLASS_NAME,self.filter_icon_classname)

    def addcart(self):
        return self.driver.find_element(By.ID,self.add_to_cart_id_p1)

    def removecart(self):
         return self.driver.find_element(By.ID, self.remove_from_cart_id_p1)

    def prod(self):
        return self.driver.find_element(By.ID,self.prod_1_id)

    def yourcart_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.your_cart_title_CSS)

    def cont_shop(self):
        return self.driver.find_element(By.ID,self.cont_shop_id)

    def checkout(self):
        return self.driver.find_element(By.ID,self.checkout_id)

    def product_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.product_title_CSS)

    def empty_cart(self):
        return self.driver.find_element(By.CLASS_NAME, self.empty_cart_class)

    def back_prod(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.back_to_products_CSS)

    def checkout_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.checkout_ur_inf0_CSS)








