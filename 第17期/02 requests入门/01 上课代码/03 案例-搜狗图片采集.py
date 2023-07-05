"""
ajax 异步加载
    在不加载整个网页的情况下, 对页面进行局部刷新
    页面上半部分数据不会刷新, 下半部分加载新数据

网站动态数据渲染:
    页面第一页数据做了静态数据渲染
    后续页数的数据统一做动态渲染
    一般情况下可以按照动态数据包翻页的规律, 构建第一页请求
"""

import requests


def get_params(page):
    """构建请求参数的函数"""
    return {
        'mood': '7',
        'dm': '0',
        'mode': '1',
        'start': str(page),
        'xml_len': '48',
        'query': '蜡笔小新'
    }

url = 'https://pic.sogou.com/napi/pc/searchList'

for i in range(0, 97, 48):
    # print(i)
    params = get_params(i)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    list_data = json_data['data']['items']
    for data in list_data:
        img_url = data['picUrl']
        print(img_url)