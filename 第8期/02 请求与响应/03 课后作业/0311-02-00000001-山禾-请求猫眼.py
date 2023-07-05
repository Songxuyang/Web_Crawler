"""
	目标地址：https://m.maoyan.com/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""

import requests
import re

url ='https://m.maoyan.com/board/4'
headers = {
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = requests.get(url, headers = headers)
response.encoding = response.apparent_encoding

rank_number = re.findall('<i class="rank-number" data-reactid=.*?>(.*?)</i>', response.text, re.S)
print(rank_number)
print(len(rank_number))

title = re.findall('<h3 class="title" data-reactid=.*?>(.*?)</h3>', response.text, re.S)
print(title)
print(len(title))

actors = re.findall('<div class="actors" data-reactid=.*?>(.*?)</div>', response.text, re.S)
print(actors)
print(len(actors))

date = re.findall('<div class="date" data-reactid=.*?>(.*?)</div>', response.text, re.S)[1:]
print(date)
print(len(date))

number = re.findall('<span class="number" data-reactid=.*?>(.*?)</span>', response.text, re.S)
print(number)
print(len(number))

for i in range(len(number)):
    with open('douban_movie.txt', 'a', encoding = 'utf-8') as f:
        f.write('{}  {}  {}  {}  {}分\n'.format(rank_number[i], title[i], actors[i], date[i], number[i]))