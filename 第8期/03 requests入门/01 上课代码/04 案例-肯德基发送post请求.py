import requests


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

"""请求参数和查询参数有区别"""
# 构建请求参数的字典 <表单数据>
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10'
}

# data 是请求参数传递的关键字
response = requests.post(url=url, data=data)
json_data = response.json()
print(json_data)

data_list = json_data['Table1']
for result in data_list:
    storeName = result['storeName']
    cityName = result['cityName']
    addressDetail = result['addressDetail']
    pro = result['pro']
    print(storeName, cityName, addressDetail, pro)
