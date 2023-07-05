import requests


response = requests.get('http://www.pcbaby.com.cn/')
# # response.encoding = response.apparent_encoding  自动识别响应体编码
# response.encoding = response.apparent_encoding
response.encoding = 'gb2312'  # 手动指定编码识别

html_str = response.text
print(html_str)

