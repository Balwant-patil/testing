# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Edge()
# driver.get("https://automation.credence.in/")
# driver.find_element(By.LINK_TEXT, "Login").click()
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
# driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
# driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# try:
#     driver.find_element(By.XPATH, "//strong[normalize-space()='These credentials do not match our records.']")
#     print("Login Test Case is Failed")
# except NoSuchElementException:
#     print("Login Test Case is Passed")
#
# driver.close()
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")

