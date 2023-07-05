"""
1. 在静态数据中, 解析所有音频的id值
2. 构建不同id, 发送音频对应的json数据的请求
3. 在请求的json数据中, 解析音频地址
4. 保存数据
"""

import requests
import parsel

# 1. 在静态数据中, 解析所有音频的id值
html_url = 'https://www.ximalaya.com/youshengshu/2684034/'

# authority 相当与host   # http2协议字段
headers = {
    'authority': 'www.ximalaya.com ',
    'cookie': '_xmLog=h5&d0223996-60af-49ff-9369-c90cecd52433&2.4.7-alpha.3; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1643118619; xm-page-viewid=ximalaya-web; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1643118759',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}

response = requests.get(url=html_url, headers=headers)
html_data = response.text
# print(html_data)

selector = parsel.Selector(html_data)
lis = selector.xpath('//li[@class="Mi_"]')

for li in lis:
    title = li.xpath('.//div[@class="text Mi_"]/a/@title').get()
    href = li.xpath('.//div[@class="text Mi_"]/a/@href').get()
    # print(title, href)

    m4a_id = href.split('/')[-1]
    # print(m4a_id)

    # 2.构建不同id, 发送音频对应的json数据的请求
    json_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={m4a_id}&ptype=1'
    response_2 = requests.get(url=json_url, headers=headers).json()
    # print(response_2)

    # 3.在请求的json数据中, 解析音频地址
    m4a_url = response_2['data']['src']
    # print(m4a_url)

    # 请求音频数据,
    m4a_data = requests.get(url=m4a_url).content

    # 4.保存数据
    with open('video\\' + title + '.m4a', mode='wb') as f:
        f.write(m4a_data)
        print('下载完成:', title)


