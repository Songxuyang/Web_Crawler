"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""
import requests

def get_page(city_name):
    """
    判断城市有多少页数据
    :param city_name: 城市名
    :return: 城市数据页数
    """
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    data = {
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10'
    }

    # data 是请求参数传递的关键字
    response = requests.post(url=url, data=data)
    json_data = response.json()
    count = json_data['Table'][0]['rowcount']
    # print(count)

    if count % 10 > 0:  # 如果数据取余10是大于零的,
        page_num = count // 10 + 1

    else:
        page_num = count // 10

    return page_num

def send_requests(city_name):
    # 获取城市有多少页数据
    page_number = get_page(city_name)  # int

    print(f'============正在获取第{city_name}地区数据==========')

    for page in range(1, page_number + 1):
        data = {
            'cname': '',
            'pid': '',
            'keyword': city_name,
            'pageIndex': str(page),  # 循环页数
            'pageSize': '10'
        }

        url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
        response = requests.post(url=url, data=data)
        json_data = response.json()
        # print(json_data)

        data_list = json_data['Table1']
        for result in data_list:
            storeName = result['storeName']
            cityName = result['cityName']
            addressDetail = result['addressDetail']
            pro = result['pro']
            print(storeName, cityName, addressDetail, pro)


if __name__ == '__main__':
    city_name_list = ['北京','上海','广州']
    # print(get_page('上海'))
    for name in city_name_list:
        send_requests(name)


