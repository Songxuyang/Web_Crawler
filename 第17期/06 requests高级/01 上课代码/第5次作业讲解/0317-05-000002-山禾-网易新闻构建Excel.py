"""
目标站点:https://news.163.com/

往下翻有 "要闻" 这个新闻类目, 找不到可以 Ctrl + F 搜索下

    需求:
        爬取网易新闻 "要闻" 类目第一页数据，将数据保存为 Excel 表格
        保存字段需要以下内容
            title
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import json
import re

import requests
import openpyxl

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
response = requests.get(url=url)
json_data = response.text
# print(json_data)

result = re.findall('data_callback\((.*?)\)', json_data, re.S)
# print(result)

item_json = json.loads(result[0])
# print(item_json)
# print(type(item_json))


work = openpyxl.Workbook()
sheet1 = work.active
sheet1.append(['title', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'])

for item in item_json:
    title = item['title']
    channelname = item['channelname']
    docurl = item['docurl']
    imgurl = item['imgurl']
    source = item['source']
    tlink = item['tlink']
    print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')
    sheet1.append([title, channelname, docurl, imgurl, source, tlink])

work.save('网易新闻.xlsx')
