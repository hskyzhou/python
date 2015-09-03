# example 1
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get("http://www.baidu.com")

##################################
# example 2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://www.yahoo.com")
assert "baidu!!!" in browser.title

elem = browser.find_element_by_name('p')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()