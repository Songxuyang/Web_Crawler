"""
ajax 异步加载:
    在不需要加载整个页面的情况下, 对页面数据进行局部刷新

    好处: 减少请求, 缓解服务器压力
    懒加载:
"""
import pprint

import requests

url = 'https://pic.sogou.com/napi/pc/searchList' # ?

def get_params(page):
    params = {
        'mode': '1',
        'start': str(page),
        'xml_len': '48',
        'query': '风景'
    }
    return params

for page in range(0, 97, 48):
    print('============================================================\n')
    params = get_params(page)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # pprint.pprint(json_data)

    data_list = json_data['data']['items']
    # print(data_list)
    for data in data_list:
        picUrl = data['picUrl']
        print(picUrl)

