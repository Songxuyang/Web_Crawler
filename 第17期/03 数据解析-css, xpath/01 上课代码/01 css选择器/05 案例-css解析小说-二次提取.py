import parsel
import requests

url = 'https://www.bqg78.com/book/1031/'
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 在解析数据前, 一定要打印数据查看是否请求到了

selector = parsel.Selector(html_data)

# 第一次数据提取: 取所有符合条件的标签
dds = selector.css('.listmain dd')  # 取所有的dd标签
print(dds)

# 第二次提取: 在标签中中取多次结果
for dd in dds:
    title = dd.css('a::text').get()
    href = dd.css('a::attr(href)').get()
    print(title, href)
