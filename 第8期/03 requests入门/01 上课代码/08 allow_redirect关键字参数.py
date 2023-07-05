import requests


url = 'http://github.com/'

# allow_redirects=False  阻止重定向
response = requests.get(url=url, allow_redirects=False)
print(response.url)
print(response.status_code)


