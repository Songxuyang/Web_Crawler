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

for i in range(1, 101):
    print('==========正在爬取第{}页=========='.format(i))
    url = 'https://www.kuaidaili.com/free/inha/{}/'.format(str(i))
    headers = {
        'Host': 'www.kuaidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html_data = response.text
    # print(html_data)

    selector = parsel.Selector(html_data)
    lis = selector.css('tbody tr')
    for li in lis:
        IP = li.css('td:nth-child(1)::text').get()
        PORT = li.css('td:nth-child(2)::text').get()
        niming = li.css('td:nth-child(3)::text').get()
        leixing = li.css('td:nth-child(4)::text').get()
        weizhi = li.css('td:nth-child(5)::text').get()
        sudu = li.css('td:nth-child(6)::text').get()
        shijian = li.css('td:nth-child(7)::text').get()
        print(IP, PORT, niming, leixing, weizhi, sudu, shijian)