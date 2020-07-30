from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('https://chercher.tech/python/windows-selenium-python')
driver.find_element_by_link_text('Handle simple Two Browser Windows / Tabs').click()
time.sleep(2)
driver.find_element_by_id('two-window').click() #open second screen
handles=driver.window_handles
driver.switch_to.window(handles[1])
print(driver.title)
driver.find_element_by_name('q').send_keys('youtube',Keys.RETURN)
time.sleep(5)
driver.close()
time.sleep(2)
driver.switch_to.window(handles[0])
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()
