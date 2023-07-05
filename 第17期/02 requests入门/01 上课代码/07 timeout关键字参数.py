import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# timeout 设置一个请求获取数据的时间, 如果超过这个时间就会报错, 报错可以用异常捕获解决
response = requests.get(url=url, headers=headers, timeout=2)
data = response.text
print(data)

