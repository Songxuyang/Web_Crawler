import requests


"""
当我们请求不到数据的时候需要考虑, 是不是被反扒了, 是不是被检测到了
"""

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Cookie': 'll="118267"; bid=VrC8tT1GWz8; __gads=ID=744f53c3cb2ebb52-22841ef3a4e00021:T=1683638065:RT=1683638065:S=ALNI_MZhRKuML1OBDnNRafe3qd6-ndhaiQ; __gpi=UID=00000c03bafcda5c:T=1683638065:RT=1683638065:S=ALNI_MbkLLsUm467wiS6ZZ6Mn2ohKIWBZw; __yadk_uid=iHqVKZD4ZHIVREbOrlu9k4uWFSsAdZtO; _pk_id.100001.4cf6=b39d476add4f5658.1683638062.; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; __utma=30149280.1169382564.1682168622.1687178001.1687181253.7; __utmb=30149280.0.10.1687181253; __utmz=30149280.1687181253.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1640817040.1683638062.1687178001.1687181253.3; __utmb=223695111.0.10.1687181253; __utmz=223695111.1687181253.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1687181253%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DujFBYcF3-z7ymnUy-5xo5XWpfNzul-nJyXI3inL3u3eedAEiRBhQ-FAXcPdn2OYL%26wd%3D%26eqid%3D836185fc0016dde800000006649057c1%22%5D; _pk_ses.100001.4cf6=1',
'Host': 'movie.douban.com',
'Pragma': 'no-cache',
'Referer': 'https://www.baidu.com/link?url=ujFBYcF3-z7ymnUy-5xo5XWpfNzul-nJyXI3inL3u3eedAEiRBhQ-FAXcPdn2OYL&wd=&eqid=836185fc0016dde800000006649057c1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'cross-site',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
}

# headers=headers 携带请求头模拟请求
response = requests.get('https://movie.douban.com/top250', headers=headers)
html_str = response.text
print(html_str)


"""
一般请求被反扒了, 有如下请求头字段, 一般都需要添加
Origin: 声明资源的起始位置
User-Agent: 浏览器的身份标识
Host: 访问的域名
Referer: 防盗链,告诉服务器从哪个页面跳转过来

Cookies: 用户身份标识, 能不加就不加
"""