import requests


def get_proxy():
    json_data = requests.get('http://demo.spiderpy.cn/get/').json()
    proxy = json_data['proxy']
    print('获取到的代理:', proxy)

    """
    proxies = {
          "http": "http://10.10.1.10:3128",
          "https": "http://10.10.1.10:1080",
        }
    """
    proxies = {
        "http": "http://" + proxy,
        "https": "http://"  + proxy,
    }
    print('规整好的代理:', proxies)
    return proxies


# get_proxy()
url = 'https://www.baidu.com/'

proxies = get_proxy()
# 找了一个第三方工具人帮助我们发送请求, 得到数据, 常用于自己电脑ip被服务器封锁的情况
response = requests.get(url=url, proxies=proxies)
print(response.text)

# 代理质量不高会报错: requests.exceptions.ProxyError, 免费代理质量不高, 经常报错, 后面我们会学习付费代理

