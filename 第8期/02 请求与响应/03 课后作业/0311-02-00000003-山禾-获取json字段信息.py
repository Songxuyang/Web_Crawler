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

url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = requests.get(url, headers = headers)

# print(response.json())
# print(type(response.json()))
result = response.json()['data'][0]
print('title:   {}'.format(result['title']))
print('picPath:   {}'.format(result['picPath']))
print('playUrl:   {}'.format(result['playUrl']))