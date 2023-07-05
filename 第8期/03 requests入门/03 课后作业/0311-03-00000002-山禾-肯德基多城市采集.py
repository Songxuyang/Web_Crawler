"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""

import requests
import pprint

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

params = {
    'op': 'keyword'
}

headers = {
    'Host': 'www.kfc.com.cn',
    'Origin': 'http://www.kfc.com.cn',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

# 获取页数
def get_page(city):
    response = requests.post(url, headers=headers, params=params, data=get_data(city, 1))
    count = response.json()['Table'][0]['rowcount']
    if count % 10 != 0:
        page = count // 10 + 1
    else:
        page = count
    return page

# 获取请求参数
def get_data(city, page):
    data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': str(page),
        'pageSize': '10'
    }
    return data
citys = ['北京', '上海', '广州']
for city in citys:
    page = get_page(city)
    for index in range(page):
        response = requests.post(url, headers=headers, params=params, data=get_data(city, index+1))
        datasets = response.json()['Table1']

        for dataset in datasets:
            address = dataset['addressDetail']
            cityName = dataset['cityName']
            pro = dataset['pro']
            provinceName = dataset['provinceName']
            rownum = dataset['rownum']
            storeName = dataset['storeName']
            print(address, cityName, pro, provinceName, rownum, storeName)