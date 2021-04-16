from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def research(error):
	search = error.replace(" ", "+")
	URL = "https://www.google.com/search?q=" + search
	driver = webdriver.Firefox()
	driver.get(URL)
	print(driver.title)


research("ID:10t error")
