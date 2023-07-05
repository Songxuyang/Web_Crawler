"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
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


count = 1  # 定义一个变量用于文件名字的指定
for i in range(0, 97, 48):
    # print(i)
    params = get_params(i)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    list_data = json_data['data']['items']
    for data in list_data:
        img_url = data['picUrl']
        print(img_url)

        try:
            # 请求图片数据
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
            img_data = requests.get(url=img_url, timeout=3, headers=headers).content
            file_name = str(count) + '.png'

            with open('img\\' + file_name, mode='wb') as f:
                f.write(img_data)

            count += 1  # 自增
        except Exception as e:
            print(e)
            continue


    print('*' * 50)

