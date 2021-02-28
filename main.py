import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Use request to get page data
DAFT_URL = "https://www.daft.ie/property-for-rent/dublin/apartments?rentalPrice_to=1000&radius=20000&sort" \
           "=publishDateDesc"
response = requests.get(DAFT_URL)
response.raise_for_status()
data = response.text

# Use bs4 to scrape info from the data
soup = BeautifulSoup(data, "html.parser")
search_result_links = soup.select(".itNYNv a")

# Get all the property links
property_links = []
for link in search_result_links:
    href = link["href"]
    if "http" not in href:
        property_links.append(f"https://www.daft.ie{href}")
    else:
        property_links.append(href)

# Get the property addresses
search_result_addresses = soup.select(".knPImU")
property_addresses = [address.get_text() for address in search_result_addresses]

# Get the property price
search_result_prices = soup.select(".gDBFnc")
property_prices = [price.get_text().strip() for price in search_result_prices]

# selenium web driver
CHROME_DRIVER_PATH = "/Users/a3ajagbe/Documents/chromedriver"
sl = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

GOOGLE_FORM_URL = "https://forms.gle/9FM28HZTs5QCFf4N9"

# Add the property address, price and link to google form
for num in range(len(property_links) - 1):
    sl.get(GOOGLE_FORM_URL)

    time.sleep(2)
    address = sl.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = sl.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = sl.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = sl.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(property_addresses[num])
    price.send_keys(property_prices[num])
    link.send_keys(property_links[num])
    submit_button.click()
