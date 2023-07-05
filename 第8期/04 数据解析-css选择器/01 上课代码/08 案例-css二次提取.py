import requests
import parsel

# 1. 找数据对应的地址
url = 'https://www.bige7.com/book/1031/'

# 2. 发送请求
response = requests.get(url=url)
html_data = response.text
print(html_data)

# 3. 数据解析
selector = parsel.Selector(html_data)

# 一次提取: 首先提取自己想要的所有标签
# 一次提取要保证提取的是标签对象 --> Selector 对象
#
dds = selector.css('.listmain dl dd')  # 提取所有的 dd 标签
# print(dds)

for dd in dds:
    # 数据的二次提取, 基于获取的对象
    title = dd.css('a::text').get()
    href = dd.css('a::attr(href)').get()
    # print(title, href)

"""
优点:
    保证数据不错乱
    结构性好
"""

"""一次性提取"""
# 组合, 麻烦点
title_2 = selector.css('.listmain dl dd a::text').getall()
href_2 = selector.css('.listmain dl dd a::attr(href)').getall()
print(title_2)
print(href_2)







