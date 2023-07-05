"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面, "时下热门" 里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		comment  评论数量
		fmplaycnt 播放量

    - 用正则表达式采集
"""
import requests

url = 'https://haokan.baidu.com/web/video/feed'
params = {
    'tab': 'gaoxiao_new',
    'act': 'pcFeed',
    'pd': 'pc',
    'num': '20',
    'shuaxin_id': '1643125398044'
}
headers = {
    'referer': 'https://haokan.baidu.com/tab/gaoxiao_new',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
response = requests.get(url, headers=headers, params=params)
data_json = response.json()
# print(data_json)
data = data_json['data']['response']['videos']
for da in data:
    title = da['title']
    duration = da['duration']
    comment = da['comment']
    fmplaycnt = da['fmplaycnt']
    print('标题：{}    时长：{}   评论数：{}    播放量：{}'.format(title, duration, comment, fmplaycnt))