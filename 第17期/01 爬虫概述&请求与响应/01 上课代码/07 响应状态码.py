import requests


response = requests.get('http://www.pcbaby.com.cn/')
print(response.status_code)

"""
100 - 200   标识服务器已经成功接受到了请求
200 - 299   表示请求成功  200  206  207
300 - 399   重定向(你请求的地址已经移动到了另外一个位置)  302
400 - 499   客户端请求的地址在服务器找不到数据<地址错了> 404 405
500 - 599   服务器错误, 是服务器问题  501  504
"""
