import requests
from bs4 import BeautifulSoup

# Use request to get page data
DAFT_URL = "https://www.daft.ie/property-for-rent/dublin/apartments?rentalPrice_to=1000"
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
    print(href)


