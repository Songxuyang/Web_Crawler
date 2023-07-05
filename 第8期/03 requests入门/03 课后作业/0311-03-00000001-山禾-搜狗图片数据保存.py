"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
import pprint

import requests

page = 0
num = 0

for i in range(0, 97, 48):
    page += 1
    url = 'https://pic.sogou.com/napi/pc/searchList'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        # 'Host': 'pic.sogou.com'
    }

    params = {
        'mode': '1',
        'start': str(i),
        'xml_len': '48',
        'query': '风景'
    }

    response = requests.get(url, headers = headers, params = params)
    # pprint.pprint(response.json())
    items = response.json()['data']['items']
    # pprint.pprint(items)
    pic = 0
    for item in items:
        num += 1
        pic += 1
        # print(item['locImageLink'])
        response = requests.get(item['locImageLink'], headers = headers)
        data = response.content
        with open('搜狗风景图/{}.jpg'.format(num), 'wb') as f:
            f.write(data)
        print('=========已录入第{}页第{}张图片========='.format(page, pic))