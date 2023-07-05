import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
params = {'op': 'keyword'}  # 查询参数
data = {  # 请求参数
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# data是构建post请求的请求参数关键字
response = requests.post(url=url, params=params, data=data, headers=headers)
json_data = response.json()
print(json_data)

list_data = json_data['Table1']
for res in list_data:
    storeName = res['storeName']
    addressDetail = res['addressDetail']
    pro = res['pro']
    print(storeName, addressDetail, pro)


"""
注意事项: 
    1. 浏览器中地址导航栏只能发送get请求
    2. 作业
    3. post请求还会有另一种请求参数<Form Data>  和 <Request Payload> --> 以json数据提交的请求参数, 用json关键字传递
"""