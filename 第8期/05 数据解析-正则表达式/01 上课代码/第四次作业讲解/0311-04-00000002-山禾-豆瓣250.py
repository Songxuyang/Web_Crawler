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


page_num = 1

for page in range(10):
    print(f'============================页数: {page}===========================')
    # 1. 请求地址
    url = f'https://movie.douban.com/top250?start={page * 25}&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }

    # 2. 发送请求
    response = requests.get(url=url, headers=headers)
    html_data = response.text
    # print(html_data)  # 在解析数据前一定要确认数据已经被我们请求到了

    # 3. 数据解析
    seletor = parsel.Selector(html_data)
    lis = seletor.css('.grid_view li')  # 一次提取, 提取所有想要的标签
    # print(divs)

    for li in lis:
        title= li.css('.hd .title:nth-child(1)::text').get()
        info= li.css('.bd p:nth-child(1)::text').getall()
        info = ' '.join([i.strip() for i in info])

        score= li.css('.rating_num::text').get()
        follow= li.css('.star span:nth-child(4)::text').get()

        print(title, info, score, follow)

    page_num += 1