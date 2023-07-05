"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}


def get_page(city_name):
    """
    传入城市名, 计算当前成一共有多少页数据
    :param city_name: 城市名
    :return: 城市对应的数据页数
    """
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    params = {'op': 'keyword'}  # 查询参数
    data = {  # 请求参数
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10'
    }

    response = requests.post(url=url, params=params, data=data, headers=headers)
    json_data = response.json()
    count = json_data['Table'][0]['rowcount']
    # print(count)

    if count % 10 > 0:  # 171取余10余1
        page_num = count // 10 + 1
    else:
        page_num = count // 10

    return page_num


# print(get_page('武汉'))

def send_request(keyword):
    page = get_page(keyword)

    for page in range(1, page + 1):
        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
        params = {'op': 'keyword'}  # 查询参数
        data = {  # 请求参数
            'cname': '',
            'pid': '',
            'keyword': keyword,
            'pageIndex': str(page),
            'pageSize': '10'
        }

        # data是构建post请求的请求参数关键字
        response = requests.post(url=url, params=params, data=data, headers=headers)
        json_data = response.json()
        # print(json_data)

        list_data = json_data['Table1']
        for res in list_data:
            storeName = res['storeName']
            addressDetail = res['addressDetail']
            pro = res['pro']
            print(storeName, addressDetail, pro)


if __name__ == '__main__':
    all_city = ['北京', '上海', '广州']
    for city in all_city:
        print(f'========================正在抓取 {city} 城市的数据======================')
        send_request(city)

