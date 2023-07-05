
# https://pic.sogou.com/pics?query=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&mood=7&dm=0&mode=1

"""
查询参数:
    在地址中如果与查询参数, 那么就是?后面的部分, 是属于查询参数
    ? 前面是请求地址, 后面是一系列的查询参数
    & 隔开每一个查询参数

    所有查询参数都是二值型的数据, key=value
"""

import requests


url = 'https://pic.sogou.com/pics?'
params = {
    'query': '蜡笔小新',
    'mood': '7',
    'dm': '0',
    'mode': '1'
}

# params 指定查询参数
# ? 可加可不加
response = requests.get(url=url, params=params)
print(response.request.url)

# https://pic.sogou.com/pics?query=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&mood=7&dm=0&mode=1
"""
在http协议中, 默认不支持中文编码, 如果请求地址中包含中文, 会自动进行url编码
url编码: 由 % + 数字 + 字母
"""

"""手动转化url编码"""
# requests.utils.quote 对中文进行url编码
print(requests.utils.quote('蜡笔小新'))

# requests.utils.unquote 对中文进行url解码
print(requests.utils.unquote('%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0'))