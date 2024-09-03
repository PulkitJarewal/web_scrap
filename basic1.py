import requests
url = "https://en.wikipedia.org/wiki/List_of_prolific_inventors"
r = requests.get(url)
print(r.text)
