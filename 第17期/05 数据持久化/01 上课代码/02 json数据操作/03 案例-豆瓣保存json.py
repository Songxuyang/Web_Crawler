import json

import parsel
import requests
import openpyxl

data = []  # 定义一个空列表, 用于收集每一条数据

for page in range(0, 226, 25):

    url = f'https://movie.douban.com/top250?start={page}&filter='
    headers = {
        'Cookie': 'll="118267"; bid=VrC8tT1GWz8; __yadk_uid=iHqVKZD4ZHIVREbOrlu9k4uWFSsAdZtO; _pk_id.100001.4cf6=b39d476add4f5658.1683638062.; __utmz=30149280.1687782730.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1687782730.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1687952054%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqdlD_RZvrHI0sXUZ08wSSKbkKLAWA_R84aALUkbWwp__yA2hUL-2C_Ej15saTpe7%26wd%3D%26eqid%3Dfdfaeaeb0001b3f60000000664998548%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1169382564.1682168622.1687782730.1687952054.9; __utmb=30149280.0.10.1687952054; __utmc=30149280; __utma=223695111.1640817040.1683638062.1687782730.1687952054.5; __utmb=223695111.0.10.1687952054; __utmc=223695111; __gads=ID=744f53c3cb2ebb52-22841ef3a4e00021:T=1683638065:RT=1687952056:S=ALNI_MZhRKuML1OBDnNRafe3qd6-ndhaiQ; __gpi=UID=00000c03bafcda5c:T=1683638065:RT=1687952056:S=ALNI_MbkLLsUm467wiS6ZZ6Mn2ohKIWBZw',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    html_data = response.text
    # print(html_data)

    """解析数据"""
    # 转对象
    selector = parsel.Selector(html_data)

    # 第一次提取
    lis = selector.css('.grid_view>li')

    # 二次提取
    for li in lis:
        title = li.css('.hd>a>span:nth-child(1)::text').get()
        info = li.css('.bd>p:nth-child(1)::text').getall()
        info = '//'.join([i.strip() for i in info])
        score = li.css('.rating_num::text').get()
        follow = li.css('.star>span:nth-child(4)::text').get()
        # print(title, info, score, follow)

        d = {'title': title, 'info': info, 'score': score, 'follow': follow}
        data.append(d)

    # print('=' * 100 + '\n')

print(data)

# json数据的序列化
json_str = json.dumps(data, ensure_ascii=False)
with open('douban.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

# [{}, {}, {}......]
