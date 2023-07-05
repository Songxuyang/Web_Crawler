
# https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&num&num2=2
# https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&num=0

"""
查询参数:
? 前面是请求地址, 后面是一系列的查询参数
& 分割开每一个查询参数

所有的查询参数都是二值型数据  key=value
"""

import requests

url = 'https://pic.sogou.com/pics?' # ?

params = {
    'query':'风景',
    'num': '0',
    'num2': ''  # 如果某个参数没有值, 那么就把值填充空字符串
}

response = requests.get(url=url, params=params)
print(response.request.url)

"""
在http协议中, 不支持中文地址的
如果地址中有中文, 会自动进行url编码 <底层>

组成: 由  [ %,字母,数字 ]  组成
"""
# requests.utils.quote  对中文进行编码
print(requests.utils.quote('风景'))

# requests.utils.unquote  对中文进行解码
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))
