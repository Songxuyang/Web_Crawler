import os.path
import re

import parsel
import requests

def change_title(title):
    pattern = re.compile("[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    new_title = re.sub(pattern, "_", title)  # 替换为下划线
    return new_title

url = 'https://www.jdlingyu.com/dm/zb'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)

# 解析数据
selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@id="post-list"]/ul/li')

for li in lis:
    # xpath语法中二次提取一定要加.
    pic_title = li.xpath('.//h2/a/text()').get()
    pic_href = li.xpath('.//h2/a/@href').get()
    print(pic_title, pic_href)

    new_title = change_title(pic_title)

    if not os.path.exists('img\\' + new_title):
        os.mkdir('img\\' + new_title)

    # 发送相册详情页请求, 因为图片地址在详情页
    response_pic = requests.get(url=pic_href, headers=headers).text

    # 解析详情页地址
    selector_pic = parsel.Selector(response_pic)

    # 提取详情页所有地址
    pic_url_list = selector_pic.xpath('//div[@class="entry-content"]//img/@src').getall()

    for pic_url in pic_url_list:
        pic_data = requests.get(url=pic_url, headers=headers).content  # 请求图片数据

        # 文件名
        file_name = pic_url.split('/')[-1]

        with open(f'img\\{new_title}\\{file_name}', mode='wb') as f:
            f.write(pic_data)
            print('下载完成:', file_name)




