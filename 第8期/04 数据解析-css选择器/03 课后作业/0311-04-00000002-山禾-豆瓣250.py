"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
"""

import requests
import parsel

url = 'https://movie.douban.com/top250'

headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
def get_params(page):
    params = {
        'start': str(page),
        'filter': ''
    }
    return params

for i in range(0, 226, 25):
    response = requests.get(url, headers=headers, params=get_params(i))
    response.encoding = response.apparent_encoding
    html_data = response.text
    # print(html_data)

    selector = parsel.Selector(html_data)
    lis = selector.css('.grid_view li')
    for li in lis:
        title = li.css('span.title:nth-child(1)::text').get()
        director = li.css('.info .bd p:nth-child(1)::text').getall()[0].strip()
        time = li.css('.info .bd p:nth-child(1)::text').getall()[1].strip().split('\\')[0]
        score = li.css('.star span:nth-child(2)::text').get()
        people = li.css('.star span:nth-child(4)::text').get()
        print(title, director, time, score, people)
        with open('douban Top250.txt', 'a', encoding='utf-8') as f:
            f.write('{}, {}, {}, {}, {}\n'.format(title, director, time, score, people))