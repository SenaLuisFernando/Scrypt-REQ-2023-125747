import time

from selenium import webdriver


driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.gsmarena.com/');

time.sleep(5) # Let the user actually see something!


search_box = driver.find_element_by_name('sSearch')

search_box.send_keys('samsung')
search_box.send_keys(Keys.RETURN)
#search_box.submit()


time.sleep(5) # Let the user actually see something!

#driver.quit()