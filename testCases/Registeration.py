# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# use chrome driver
driver = webdriver.Edge()

# assign web page url
driver.get("http://demo.automationtesting.in/Windows.html")

# find XPath

# driver.find_element(By.XPATH,"//a[normalize-space()='WebTable']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
# driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

# return all handles value of open browser window
handles = driver.window_handles

for i in handles:
	driver.switch_to.window(i)

	# close specified web page
	if driver.title == "Frames & windows":
		time.sleep(2)
		driver.close()
