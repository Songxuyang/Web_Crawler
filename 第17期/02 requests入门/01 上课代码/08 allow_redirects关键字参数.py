import requests

url = 'http://github.com/'

# allow_redirects默认是True, 自动重定向; 如果设置为False, 那么会阻止重定向
response = requests.get(url=url, allow_redirects=False)
print(response.request.url)

