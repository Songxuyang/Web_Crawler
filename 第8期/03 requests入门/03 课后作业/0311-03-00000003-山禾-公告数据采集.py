"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出即可
请在下方完成代码:
"""
import pprint

import requests


headers = {
    'Cookie': '_zcy_log_client_uuid=bfc9efb0-79fa-11ec-82b0-3bd7f6a37b7c',
    'Host': 'www.zfcg.sh.gov.cn',
    'Origin': 'http://www.zfcg.sh.gov.cn',
    'Referer': 'http://www.zfcg.sh.gov.cn/ZcyAnnouncement/index.html?utm=sites_group_front.2ef5001f.0.0.bfcc39a079fa11ec82b03bd7f6a37b7c',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
def get_json(page):
    json = {
        'categoryCode': "ZcyAnnouncement3012",
        'pageNo': str(page),
        'pageSize': '15',
        'utm': "sites_group_front.2ef5001f.0.0.dbfbe1c07b3a11ec8c623beb442d38e6"
    }
    return json
for page in range(1, 58):
    url = 'http://www.zfcg.sh.gov.cn/front/search/category'
    print('=========正在爬取第{}页=============='.format(page))
    response = requests.post(url, headers=headers, json=get_json(page))
    response.encoding = response.apparent_encoding
    # pprint.pprint(response.json())
    data_json = response.json()['hits']['hits']

    for data in data_json:
        title = data['_source']['title']
        url = data['_source']['url']
        districtName = data['_source']['districtName']
        print(title, url, districtName)