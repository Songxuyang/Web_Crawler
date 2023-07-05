"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import csv
import json
import re

import requests
import openpyxl

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
response = requests.get(url=url)
json_data = response.text

result = re.findall('data_callback\((.*?)\)', json_data, re.S)

item_json = json.loads(result[0])

with open('网易新闻.csv', mode='a', encoding='utf-8', newline='') as f:
    write = csv.writer(f)
    write.writerow(['title', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'])

    for item in item_json:
        title = item['title']
        channelname = item['channelname']
        docurl = item['docurl']
        imgurl = item['imgurl']
        source = item['source']
        tlink = item['tlink']
        print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')

        write.writerow([title, channelname, docurl, imgurl, source, tlink])
