import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

tit = soup.find_all("a",class_ = "title")
product_tit = []
for ti in tit:
    product_tit.append(ti.string)

# print(product_tit)


pric = soup.find_all("h4",class_ = "price float-end card-title pull-right")
product_price = []
for pi in pric:
    product_price.append(pi.string)

# print(product_price)

df = pd.DataFrame({"Title" : product_tit, "Price" :  product_price})
print(df)

df.to_excel("web_scrp_tut.xlsx")
