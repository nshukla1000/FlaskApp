import random
print(random.randint(1, 6))
q= random.randint(1, 6)
print (q)

import requests
#from bs4 import BeautifulSoup

# libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


#result = requests.get('https://www.whitehouse.gov/briefings-statements')
result = requests.get('https://www.southwest.com/air/booking/select.html?int=HOMEQBOMAIR&adultPassengersCount=1&departureDate=2020-05-31&destinationAirportCode=HOU&fareType=USD&originationAirportCode=DAL&passengerType=ADULT&returnDate=&seniorPassengersCount=0&tripType=oneway&departureTimeOfDay=ALL_DAY&reset=true&returnTimeOfDay=ALL_DAY')
#result = requests.get('https://book.goindigo.in/Flight/PriceItineraryAEM?SellKeys%5B%5D=0~R~%20~6E~R0IP~1057~~0~3~~X|6E~5339~%20~~DEL~06/03/2020%2009:25~BOM~06/03/2020%2011:45~~')
src = result.content
#print(src)
soup = BeautifulSoup(src, 'html.parser')
x=soup.prettify()
#print(x)
urls=[]
containers = soup.find_all('div', class = "row trips-row d-flex")
print('length is :', len(containers))
for h2_tag in soup.find_all('li'):
#for h2_tag in soup.find_all('li', attrs={'class' : "air-booking-select-detail air-booking-select-detail_min-products air-booking-select-detail_min-duration-and-stops" }):
    #a_tag = h2_tag.find('a')
    a_tag = h2_tag.find_all('div', {'class' : "air-operations-time-status air-operations-time-status_booking-primary select-detail--time" })
    print ("Here", a_tag)
    #urls.append(a_tag.attrs['href'])

print(urls)

#<li class="air-booking-select-detail air-booking-select-detail_min-products air-booking-select-detail_min-duration-and-stops"><div class="select-detail--indicators"><div class="air-operations-flight-numbers air-operations-flight-numbers_select-detail select-detail--flight-numbers" id="air-booking-flight-number-0-1" type="select-detail"><div class="flyout-trigger flight-numbers--trigger"><button aria-label="Information for flight number 1. Opens flyout." class="actionable actionable_button actionable_light button flight-numbers--flight-number" aria-expanded="false" type="button" data-a="flight-numbers-flyout"><span class="actionable--text"><!-- react-text: 776 --># 1<!-- /react-text --></span><span class="swa-g-screen-reader-only">&nbsp;Opens flyout.</span></button></div></div><div class="flight-stops-badge flight-stops-badge_nonstop select-detail--flight-stops-badge">Nonstop</div></div><div class="air-operations-time-status air-operations-time-status_booking-primary select-detail--time" type="origination"><span class="time--value"><span class="swa-g-screen-reader-only">Departs </span><!-- react-text: 782 -->7:00<!-- /react-text --><span class="time--period">AM</span></span></div><span class="swa-icon swa-icon_micro select-detail--pointer swa-icon_pointer" icon="swa-icon_pointer" role="presentation"><span role="presentation" class="swa-icon--icon"></span></span><div class="air-operations-time-status air-operations-time-status_booking-primary select-detail--time" type="destination"><span class="time--value"><span class="swa-g-screen-reader-only">Arrives </span><!-- react-text: 789 -->8:05<!-- /react-text --><span class="time--period">AM</span></span></div><div class="flight-stops flight-stops_duration-and-stops-summary select-detail--stops"><div class="flight-stops--duration"><!-- react-text: 793 -->Duration<!-- /react-text --><span class="flight-stops--duration-time">1h 5m</span></div><div class="flight-stops--items"><span class="flight-stops--departure"></span><span class="flight-stops--split"></span><span class="flight-stops--arrival"></span></div></div><div class="select-detail--fares" id="air-booking-fares-0-1"><div class="fare-button fare-button_primary-blue select-detail--fare"><button class="actionable actionable_button fare-button--button" aria-label="Business Select ® fare $274, earn 3167 points with this purchase. Navigate to the content below to learn more about the fare benefits. Select to add item to cart."><span class="actionable--text"><span class="fare-button--text"><span class="fare-button--value"><span class="currency currency_dollars"><span class="swa-g-screen-reader-only"><!-- react-text: 807 -->274 Dollars<!-- /react-text --></span><span aria-hidden="true"><span class="currency--symbol">$</span><span class="">274</span></span></span></span></span></span></button></div><div class="fare-button fare-button_secondary-light-blue select-detail--fare"><button class="actionable actionable_button fare-button--button" aria-label="Anytime fare $244, earn 2339 points with this purchase. Navigate to the content below to learn more about the fare benefits. Select to add item to cart."><span class="actionable--text"><span class="fare-button--text"><span class="fare-button--value"><span class="currency currency_dollars"><span class="swa-g-screen-reader-only"><!-- react-text: 818 -->244 Dollars<!-- /react-text --></span><span aria-hidden="true"><span class="currency--symbol">$</span><span class="">244</span></span></span></span></span></span></button></div><div class="fare-button fare-button_primary-yellow select-detail--fare"><button class="actionable actionable_button fare-button--button" aria-label="Wanna Get Away ® fare $129, earn 714 points with this purchase. Navigate to the content below to learn more about the fare benefits. Select to add item to cart."><span class="actionable--text"><span class="fare-button--text"><span class="fare-button--value"><span class="currency currency_dollars"><span class="swa-g-screen-reader-only"><!-- react-text: 829 -->129 Dollars<!-- /react-text --></span><span aria-hidden="true"><span class="currency--symbol">$</span><span class="">129</span></span></span></span></span></span></button></div></div></li>
#<div class="air-operations-time-status air-operations-time-status_booking-primary select-detail--time" type="origination"><span class="time--value"><span class="swa-g-screen-reader-only">Departs </span><!-- react-text: 782 -->7:00<!-- /react-text --><span class="time--period">AM</span></span></div>