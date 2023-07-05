# http://www.gebiqu.com/biquge_207056/44547067.html

import requests



response = requests.get('http://www.gebiqu.com/biquge_207056/44547067.html')
# 方式一:自动识别
# response.encoding = response.apparent_encoding  # 自动识别响应体编码

# 方式二:自动识别
response.encoding = 'utf-8'


print(response.text)
