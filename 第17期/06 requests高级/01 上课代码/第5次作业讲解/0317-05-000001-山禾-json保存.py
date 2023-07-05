"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	请求方式: GET
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串
			
请在下方编写代码
"""
import requests


url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
response = requests.get(url=url)
json_data = response.text
print(json_data)

with open('data.json',  mode='w', encoding='utf-8') as f:
    f.write(json_data)

# json序列化-