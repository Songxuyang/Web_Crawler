import requests

"""获取代理"""
def get_proxy():
  proxy_url = 'http://demo.spiderpy.cn/get/'
  json_data = requests.get(url=proxy_url).json()
  proxy = json_data['proxy']
  # print(proxy)
  return proxy


proxy = get_proxy()

# 构建代理的形式
proxies = {
  "http": "http://" + proxy,
  "https": "http://" + proxy,
}

# proxies  请求添加代理的关键字
# 如果代理质量不好的就会报错 requests.exceptions.ProxyError
baidu_response = requests.get("https://www.baidu.com", proxies=proxies, verify=False)
print(baidu_response)
print(baidu_response.status_code)