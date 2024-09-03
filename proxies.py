# import requests

# proxies = {
#    'http': 'http://proxy.example.com:8080',
#    'https': 'http://secureproxy.example.com:8090',
# }

# url = 'http://mywebsite.com/example'

# response = requests.post(url, proxies=proxies)

import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

requests.get("http://example.org", proxies=proxies)
