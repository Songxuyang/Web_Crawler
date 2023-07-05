"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	发送 GET 请求

	要求：
		1、请求上述网址的数据
		2、按照要求提取以下字段信息
			title、
			picPath、
			playUrl
		提取下来用 print() 函数打印即可
请在下方编写代码
"""
import requests
import pprint

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'


response = requests.get(url)
data = response.json()  # json()  会在底层自动把字符串的json转换成对象
pprint.pprint(data)  # 格式化输出打印

data_list = data['data']

for data_ in data_list:
    title = data_['title']  # 字典取值
    picPath = data_['picPath']
    playUrl = data_['playUrl']
    print(title, picPath, playUrl)

