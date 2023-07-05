import requests
import parsel

# 1. 找数据对应的地址
url = 'https://www.bige7.com/book/1031/1.html'

# 2. 发送请求
response = requests.get(url=url)
html_data = response.text
# print(html_data)

# 在数据解析之前, 我们一定要做一件事情, 要确认请求的数据中有我们要的数据
# 3. 数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)

name = selector.css('.content h1.wap_none').getall()
# print(name)

name = selector.css('#chaptercontent::text').getall()
# print(name)

en = selector.css('.this a::text').get()
print(en)





