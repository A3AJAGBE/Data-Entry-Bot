import requests
from bs4 import BeautifulSoup

# Use request to get page data
DAFT_URL = "https://www.daft.ie/property-for-rent/dublin/apartments?rentalPrice_to=1000"
response = requests.get(DAFT_URL)
response.raise_for_status()
data = response.text



