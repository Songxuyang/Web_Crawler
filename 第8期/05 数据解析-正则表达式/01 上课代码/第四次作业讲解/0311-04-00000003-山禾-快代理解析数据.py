"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
"""
import requests
import parsel


# 1. 请求地址
url = 'https://www.kuaidaili.com/free/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)  # 在解析数据前一定要确认数据已经被我们请求到了

# 3. 数据解析
seletor = parsel.Selector(html_data)
divs = seletor.css('tbody>tr')  # 一次提取, 提取所有想要的标签
print(divs)
print(len(divs))

for div in divs:
    ip = div.css('td:nth-child(1)::text').get()
    port = div.css('td:nth-child(2)::text').get()
    type_ = div.css('td:nth-child(4)::text').get()
    print(ip, port, type_)