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


# 1. 请求地址
url = 'https://m.maoyan.com/board/4'
headers = {
    'Cookie': 'uuid_n_v=v1; iuuid=BDAB8D50791A11EC8741DBA2CF60E163B1A8687D291B4069B1D01A6E824A0D3B; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; webp=true; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1642591631,1643024139; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1643024139; _last_page=undefined',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)  # 在解析数据前一定要确认数据已经被我们请求到了

# 3. 数据解析
seletor = parsel.Selector(html_data)
divs = seletor.css('.clearfix')  # 一次提取, 提取所有想要的标签
# print(divs)

for div in divs:
    name = div.css('.title::text').get()
    star = div.css('.actors::text').get()
    releasetime = div.css('.date::text').get()
    score = div.css('.number::text').get()
    # score

    print(name, star, releasetime, score)

