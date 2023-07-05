"""
    使用 css 选择器将猫眼 100 全部电影信息全部提取出来。
    目标网址：https://m.maoyan.com/board/4

    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
"""
import requests
import parsel

url = 'https://m.maoyan.com/board/4'
headers = {
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)
selector = parsel.Selector(html_data)
lis = selector.css('.board-card.clearfix')
for li in lis:
    rank = li.css('.cover .rank-number::text').get()
    title = li.css('.info .title::text').get()
    actors = li.css('.info .actors::text').get()
    date = li.css('.info .date::text').get()
    score = li.css('span.number::text').get() + '分'
    print(rank, title, actors, date, score)
    with open('maoyan Top100.txt', 'a', encoding='utf-8') as f:
        f.write('{}, {}, {}, {}, {}\n'.format(rank, title, actors, date, score))