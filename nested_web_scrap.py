import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

spes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")[3]
print(spes.text)
