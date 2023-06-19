from selenium.webdriver.common.by import By

class Login:
  user_name_id='user-name'
  password_id='password'
  login_button_id='login-button'
  product_title_CSS='#header_container > div.header_secondary_container > span'

  def __init__(self,driver):
    self.driver=driver

  def username(self,username):
    self.driver.find_element(By.ID,self.user_name_id).send_keys(username)

  def password(self,password):
      self.driver.find_element(By.ID,self.password_id).send_keys(password)

  def click(self):
      self.driver.find_element(By.ID,self.login_button_id).click()

  def prod_title(self):
      return self.driver.find_element(By.CSS_SELECTOR,self.product_title_CSS)
