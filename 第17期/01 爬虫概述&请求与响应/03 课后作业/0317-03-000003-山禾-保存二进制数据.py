"""
	目标网址：https://ibaotu.com/sucai/19838349.html
	
	要求：
		1、在上述目标网址中找到视频的数据包
		2、用requests模块模拟请求视频数据并且保存下来
		
请在下方编写代码
"""

import requests

headers = {
    'Origin': 'https://ibaotu.com',
    'Referer': 'https://ibaotu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
response = requests.get('https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4', headers=headers)
content = response.content

with open('result.mp4', 'wb') as f:
    f.write(content)