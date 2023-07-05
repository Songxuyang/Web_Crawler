import parsel
import requests

url = 'https://www.bqg78.com/book/1031/1.html'
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 在解析数据前, 一定要打印数据查看是否请求到了

selector = parsel.Selector(html_data)
title = selector.css('h1.wap_none::text').getall()
print(title)

contend = selector.css('#chaptercontent::text').getall()
print(contend)
