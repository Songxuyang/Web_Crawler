import requests

proxy_response = requests.get('http://127.0.0.1:5010/get')
proxy = proxy_response.json()
print(proxy)

"""
如果目标计算机积极拒绝 --> requests.exceptions.ConnectionError:
    此问题是你在服务器没有权限
    或者服务器没有服务程序
"""