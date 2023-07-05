"""
将上课的案例-爬取小说完善。爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""

import requests
import re

url = 'https://www.bige7.com/book/1031/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

response = requests.get(url, headers=headers)

html_data = response.text
# print(html_data)


title = re.findall('<dd><a href ="/book/1031/.*?.html">(.*?)</a></dd>', html_data, re.S)[:10]
# print(title)

# url = 'https://www.bige7.com/book/1031/1.html'
# response = requests.get(url, headers=headers)
# print(response.text)

# result = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)\r', response.text,re.S)[0]
# result = result.replace('\u3000\u3000', '').replace('<br /><br />', '')
# print(result)

for i in range(1, 11):

    new_url = 'https://www.bige7.com/book/1031/{}.html'.format(str(i))
    response = requests.get(new_url, headers=headers)
    result = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)\r', response.text, re.S)[0]
    result = result.replace('\u3000\u3000', '').replace('<br /><br />', '\n')
    with open('./作业1/{}.txt'.format(title[i-1]), 'w', encoding='utf-8') as f:
        f.write(result)
        print('=========第{}章已录入========='.format(i))