from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('C:\\Users\e105356\Documents\Temp\chromedriver.exe') 
driver.get('https://www.southwest.com/air/booking/select.html?int=HOMEQBOMAIR&adultPassengersCount=1&departureDate=2020-05-31&destinationAirportCode=HOU&fareType=USD&originationAirportCode=DAL&passengerType=ADULT&returnDate=&seniorPassengersCount=0&tripType=oneway&departureTimeOfDay=ALL_DAY&reset=true&returnTimeOfDay=ALL_DAY')
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "air-operations-time-status air-operations-time-status_booking-primary select-detail--time")))
except TimeoutException:
    print('Page timed out after 10 secs.')
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(driver.page_source)
driver.quit()
# print(soup.find('a', {'data-a-target': 'clip-thumbnail-link'})['href'])  

#<div class="air-operations-time-status air-operations-time-status_booking-primary select-detail--time" type="origination"><span class="time--value"><span class="swa-g-screen-reader-only">Departs </span><!-- react-text: 662 -->7:00<!-- /react-text --><span class="time--period">AM</span></span></div>