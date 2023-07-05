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
import re

import requests



url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1643112137562'

response = requests.get(url=url)
json_data = response.json()
# print(json_data)
# print(type(json_data))

"""
\{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)', .*?'comment': '(.*?)', .*?'fmplaycnt': '(.*?)',.*?\}
"""
pattern = "\{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)', .*?'comment': '(.*?)', .*?'fmplaycnt': '(.*?)',.*?\}"

json_str = str(json_data)
# print(json_str)
result = re.findall(pattern, json_str, re.S)
print(result)






