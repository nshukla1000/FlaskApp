import time
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\e105356\Documents\Temp\chromedriver.exe')  # Optional argument
driver.get('https://www.walmart.com/browse/electronics/windows-10-laptops/3944_3951_1089430_1230457?cat_id=3944_3951_1089430_1230457&facet=memory_capacity%3A8+GB%7C%7Cprice%3A%240+-+%24200%7C%7Cprocessor_type%3AIntel+Core+i5%7C%7Chard_drive_capacity_component_hard_drive%3A500GB+-+640GB')
time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()