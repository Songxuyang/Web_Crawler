"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出即可
"""
import requests


for page in range(1, 3):
    print('===========================================================================\n')
    url = 'http://www.zfcg.sh.gov.cn/front/search/category'

    data_json = {
        'categoryCode': "ZcyAnnouncement3012",
        'pageNo': str(page),
        'pageSize': '15',
        'utm': "sites_group_front.2ef5001f.0.0.98c83df07ab211ec94b6d3c7f7ac800e"
    }

    data_json_2 = {"utm":"sites_group_front.2ef5001f.0.0.98c83df07ab211ec94b6d3c7f7ac800e","categoryCode":"ZcyAnnouncement3012","pageSize":15,"pageNo":1}

    response = requests.post(url=url, json=data_json)
    json_data = response.json()
    # print(json_data)

    list_data = json_data['hits']['hits']
    # print(list_data)

    for data in list_data:
        title = data['_source']['title']
        url = data['_source']['url']
        districtName = data['_source']['districtName']
        print(title, url, districtName)







