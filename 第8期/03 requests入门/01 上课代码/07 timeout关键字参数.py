import requests


url = 'https://github.com/'

try:
    # timeout=1   设置请求的时间, 单位秒, 超过这个时间, 程序会报错
    response = requests.get(url=url, timeout=1)
    html_data = response.text
    print(html_data)
except Exception as e:
    print(e)


