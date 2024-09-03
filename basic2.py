import requests

def fetchAndSave(url, path):
    r = requests.get(url)
    with open(path,"w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://en.wikipedia.org/wiki/List_of_prolific_inventors"
fetchAndSave(url,"fetch/file.html")
