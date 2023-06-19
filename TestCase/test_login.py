from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import openpyxl
service1=Service(executable_path="C:\\Users\\hp\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
from PageObj.Loginpage import Login
from Utilities.XLUtils import XLUtils

class Test_login_01:
  baseurl='https://www.saucedemo.com/'
  username='standard_user'
  password='secret_sauce'
  path="./TestData/testdata.xlsx"

  def test_title(self):
     self.driver = webdriver.Chrome(service=service1)
     self.driver.get(self.baseurl)
     if self.driver.title=='Swag Labs':
         print(self.driver.title)
         assert True
     else:
         self.driver.save_screenshot('.\\Screenshoots\\'+'test_titie.png')
         self.driver.close()
         assert False


  def test_login(self):
     self.driver=webdriver.Chrome(service=service1)
     self.driver.get(self.baseurl)
     self.obj=Login(self.driver)
     for r in range(2,7):
        self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
        self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
        self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
        self.obj.username(self.username)
        self.obj.password(self.password)
        self.obj.click()
        title=self.obj.prod_title()
        act_title =title.text
        exp_title ='Products'

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


     





