import pandas as pd 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.mahindrafirstchoice.com/used-cars/delhi'

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

driver.get(url)
time.sleep(4)

no_of_pagedowns = 15
year = []
prices = []
carMakes = []
carModels = []
location = []
kilometers = []
fuel = []
btype = []
owner = []

elem = driver.find_element_by_tag_name("body")

driver.minimize_window()

for i in range(no_of_pagedowns):
    time.sleep(1)
    
    try:
        carMake = driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[1]/a[1]/h3')
        carMakes.append(carMake.text)
    except:
        carMakes.append('None')
    
    try:
        carModel = driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[1]/a[2]/h3')
        carModels.append(carModel.text)
    except:
        carModels.append('None')
    
    try:
        price = driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/div[2]/span[1]/span')
        prices.append(price.text)
    except:
        prices.append('None')

    try:
        location.append(driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/div[2]/span[3]/span').text)
    except:
        location.append('None')
    
    try:
        kilometers.append(driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/ul/li[1]/span[2]').text)
    except:
        kilometers.append('None')

    try:
        fuel.append(driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/ul/li[2]/span[2]').text)
    except:
        fuel.append('None')
    try:
        btype.append(driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/ul/li[3]/span[2]').text)
    except:
        btype.append('None')    

    try:
        owner.append(driver.find_element_by_xpath(f'//*[@id="buyer_stock_results"]/div/div[{i+1}]/div/div[3]/ul/li[4]/span[2]').text)
    except:
        owner.append('None')

    time.sleep(1)
    elem.send_keys(Keys.PAGE_DOWN)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    print(f'round {i+1} done...')

d = {
    'carmake': carMakes,
    'carmodel': carModels,
    'prices': prices,
    'location': location,
    'kilometers': kilometers,
    'fuelType': fuel,
    'bodyType': btype,
    'owner': owner
}

# print(
#     carMakes,
#     carModels,
#     prices,
#     location,
#     kilometers,
#     fuel,
#     btype,
#     owner
# )

df = pd.DataFrame(d)
print(df)
df.to_csv('UsedCars.csv')