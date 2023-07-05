"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                districtName 公告区域
            3. 采集完后打印输出即可
请在下方完成代码:
"""
import requests

url = 'http://www.zfcg.sh.gov.cn/portal/category'

json_data = {"pageNo": 1, "pageSize": 15, "categoryCode": "ZcyAnnouncement1", "_t": 1687780627000}

# json 以json数据提交的请求参数
response = requests.post(url=url, json=json_data)
json_data = response.json()
print(json_data)

for data in json_data['result']['data']['data']:
    title = data['title']
    districtName = data['districtName']
    print(title, districtName)
