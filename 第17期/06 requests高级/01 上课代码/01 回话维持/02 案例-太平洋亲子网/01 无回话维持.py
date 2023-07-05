
"""
官网地址: https://www.pcbaby.com.cn/
个人中心页面地址: https://my.pcbaby.com.cn/user/adminIndex.jsp
登录页面地址: http://my.pcbaby.com.cn/login.jsp?return=http%3A%2F%2Fmy.pcbaby.com.cn%2Fuser%2FadminIndex.jsp

账号: mb51222353
密码: 123456..
"""

import requests


my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
response = requests.get(url=my_home_url, headers=headers)
print(response.text)
print(response.status_code)

with open('my_home.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)

"""
当我们没有登录的时候, 请求个人中心页面的数据会自动的重定向
"""

