# libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# use chrome extension
driver = webdriver.Chrome("C:\\Users\e105356\Documents\Temp\chromedriver.exe")

# getData
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
#driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr\?sid=6bo%2Cb5g&uniq")
#driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')
driver.get('https://www.walmart.com/browse/electronics/windows-10-laptops/3944_3951_1089430_1230457?cat_id=3944_3951_1089430_1230457&facet=memory_capacity%3A8+GB%7C%7Cprice%3A%240+-+%24200%7C%7Cprocessor_type%3AIntel+Core+i5%7C%7Chard_drive_capacity_component_hard_drive%3A500GB+-+640GB')
# Extract data
content = driver.page_source
soup = BeautifulSoup(content)
print("here1")
for a in soup.findAll('a',href=True, attrs={'class':'search-result-gridview-items four-items'}):
    name=a.find('div', attrs={'class':'product-title-link'})
    price=a.find('div', attrs={'class':'product-price-with-fulfillment'})
    #rating=a.find('div', attrs={'class':'VGWI6T'})
    print("here2")
    print(name, " ", price, " ")
    products.append(name.text)
    prices.append(price.text)
    #ratings.append(rating.text) 
driver.quit()
# save to file
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
