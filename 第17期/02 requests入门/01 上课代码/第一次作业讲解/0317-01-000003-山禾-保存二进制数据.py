"""
	目标网址：https://ibaotu.com/sucai/19838349.html
	
	要求：
		1、在上述目标网址中找到视频的数据包
		2、用requests模块模拟请求视频数据并且保存下来
		
请在下方编写代码
"""
import requests

url = 'https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4'
response = requests.get(url)
video_data = response.content

file_name = url.split('/')[-1]
# 准备保存视频的文件名字
with open(file_name, mode='wb') as f:
    f.write(video_data)