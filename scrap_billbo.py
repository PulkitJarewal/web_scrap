import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.billboard.com/charts/hot-100/"

f = requests.get(url)

soup = BeautifulSoup(f.text,'html.parser')

song_nm = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s")
artist_nm = soup.select("span.c-label.a-no-trucate.a-font-primary-s")

data = {'Song':[], 'Artist':[]}

for indi in song_nm:
    data['Song'].append(indi.string.strip())

for indi in artist_nm:
    data['Artist'].append(indi.string.strip())

df = pd.DataFrame.from_dict(data) 
df.to_excel("data.xlsx", index=False)
        
