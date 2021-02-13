from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import requests


header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language" :"en-US,en;q=0.9"
}

zillow_url = "https://www.zillow.com/toronto-on/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.79661155078125%2C%22east%22%3A-78.95615744921875%2C%22south%22%3A43.30868669437285%2C%22north%22%3A44.10483987547455%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"


response = requests.get(zillow_url, headers=header)
response.raise_for_status()

data = response.text
soup = BeautifulSoup(data, 'html.parser')

all_link_elements = soup.select(".list-card-top a")
all_links = []

for link in all_link_elements:
    href = link['href']
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links)

all_addresses_elements = soup.select(".list-card-addr")
all_addresses = [address.get_text() for address in all_addresses_elements]


print(all_addresses)

all_link_prices_elements = soup.select(".list-card-price")
all_prices =[]


for listing_prices in all_link_prices_elements:
    prices = listing_prices.get_text()
    cost_prices = int(prices.split('$')[1].replace('/', '').replace('+', '').replace('mo', '').split()[0].replace(',', ''))
    all_prices.append(cost_prices)

print(all_prices)


chrome_driver_path = "C:\\ChromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://docs.google.com/forms/viewform")

for n in range(len(all_links)):

    time.sleep(2)
    faddress = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    faddress.send_keys(all_addresses[n])

    fprice = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    fprice.send_keys(all_prices[n])

    flinks = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    flinks.send_keys(all_links[n])

    subBtn = driver.find_element_by_css_selector('.appsMaterialWizButtonPaperbuttonLabel')
    subBtn.click()
    resubmit = driver.find_element_by_link_text("Submit another response")
    resubmit.click()

driver.close()

