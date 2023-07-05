
"""
官网地址: https://www.pcbaby.com.cn/
个人中心页面地址: https://my.pcbaby.com.cn/user/adminIndex.jsp
登录页面地址: http://my.pcbaby.com.cn/login.jsp?return=http%3A%2F%2Fmy.pcbaby.com.cn%2Fuser%2FadminIndex.jsp

账号: mb51222353
密码: 123456..
"""

import requests

# def get_proxy():
#     url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=1&sb=&mr=2&sep=0'
#     response = requests.get(url=url)
#     json_data = response.json()
#     # print(json_data)
#
#     ip_port = json_data['data'][0]['ip'] + ":" + str(json_data['data'][0]['port'])
#     # print(ip_port)
#
#     proxies = {
#         "http": "http://" + ip_port,
#         "https": "http://"  + ip_port,
#     }
#     return proxies
#
# proxies = get_proxy()
# print('获取到的代理:', proxies)


session = requests.Session()

headers = {
    # 'Cookie': 'u=35glx62u; c=36glwvep; pcsuv=1681996661754.a.77080874; slidecaptcha=bec8e1757a0944a7b880d4dea214a8d8; cmu=mb51222353; pcsuv2=1688389738448.a.99790086; pcuvdata=lastAccessTime=1688389738448|visits=3; channel=3794',
    'Host': 'passport3.pcbaby.com.cn',
    'Origin': 'http://my.pcbaby.com.cn',
    'Referer': 'http://my.pcbaby.com.cn/login.jsp?return=http%3A%2F%2Fmy.pcbaby.com.cn%2Fuser%2FadminIndex.jsp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}


"""模拟登录"""
login_url = 'http://passport3.pcbaby.com.cn/passport3/passport/login_ajax_do_new.jsp?req_enc=UTF-8'
data = {
    'return': 'https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'bindUrl': 'https://my.pcbaby.com.cn/passport/bindMobile.jsp?return=https://my.pcbaby.com.cn/user/adminIndex.jsp',
    'username': 'mb51222353',
    'password': '123456..',
    'auto_login': '30',
    'checkbox': 'on',
}

login_response = session.post(url=login_url, data=data, headers=headers)
print(login_response.json())
print(login_response.status_code)


"""
如果直接用requests请求, 那么上下的这两次请求是没有半毛钱关系的 √
需要用回话维持
"""
"""请求个人中心页面"""
my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
response = session.get(url=my_home_url)
print(response.text)
print(response.status_code)

with open('my_home_2.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)

"""
当我们没有登录的时候, 请求个人中心页面的数据会自动的重定向
"""

