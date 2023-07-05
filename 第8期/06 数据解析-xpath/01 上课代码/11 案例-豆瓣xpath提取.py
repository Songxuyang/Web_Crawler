import requests
import parsel





# 1. 请求地址
url = f'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)  # 在解析数据前一定要确认数据已经被我们请求到了

# 3. 数据解析
seletor = parsel.Selector(html_data)
lis = seletor.xpath('//*[@class="grid_view"]//li')  # 一次提取, 提取所有想要的标签
# print(divs)

for li in lis:  # 二次提取
    title= li.xpath('.//*[@class="hd"]//*[@class="title"][1]/text()').get()
    # info= li.xpath('.bd p:nth-child(1)::text').getall()
    # info = ' '.join([i.strip() for i in info])
    #
    # score= li.xpath('.rating_num::text').get()
    # follow= li.xpath('.star span:nth-child(4)::text').get()

    print(title)