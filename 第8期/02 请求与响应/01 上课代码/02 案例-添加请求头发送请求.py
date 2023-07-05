# https://movie.douban.com/top250

import requests

"""
爬虫: 模拟客户端请求服务器数据

为什么请求不到数据?
    是不是服务器没有响应?
    
    是不是遇到了反扒 ---> 服务器有可能设置反扒策略
        是不是我的身份在服务器过不了关?
      
"""

# 请求头需要构建成字典
headers = {
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'zh-CN,zh;q=0.9',
    #'Cache-Control': 'no-cache',
    #'Connection': 'keep-alive',
    #'Cookie': 'bid=avtp9Di-DDY; __gads=ID=2ad63904814bc4e1-22dc0248d4cf00ad:T=1642165455:RT=1642165455:S=ALNI_MafrXzI8HJAwP5WQE1xZ0MARt8BfQ; __utma=30149280.861056058.1642165455.1642165455.1642424351.2; __utmb=30149280.0.10.1642424351; __utmc=30149280; __utmz=30149280.1642424351.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.151617039.1642165455.1642165455.1642424351.2; __utmb=223695111.0.10.1642424351; __utmc=223695111; __utmz=223695111.1642424351.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1642424351%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DlDlTVWragaYFBVncmBlLaPC9FxfghgE8ddR27aCHt8rf81lBCh5nanctaSGXccYK%26wd%3D%26eqid%3Dc44c40170000a0460000000661e5681d%22%5D; _pk_id.100001.4cf6=d879380485021ab2.1642165454.2.1642424351.1642165850.; _pk_ses.100001.4cf6=*; ap_v=0,6.0',
    'Host': 'movie.douban.com',
    #'Pragma': 'no-cache',
    'Referer': 'https://www.baidu.com/link?url=lDlTVWragaYFBVncmBlLaPC9FxfghgE8ddR27aCHt8rf81lBCh5nanctaSGXccYK&wd=&eqid=c44c40170000a0460000000661e5681d',
    #'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    #'sec-ch-ua-mobile': '?0',
    #'sec-ch-ua-platform': '"Windows"',
    #'Sec-Fetch-Dest': 'document',
    #'Sec-Fetch-Mode': 'navigate',
    #'Sec-Fetch-Site': 'cross-site',
    #'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

# 请求的时候做了伪装, 能够在一定程度上解决反扒
response = requests.get('https://movie.douban.com/top250', headers=headers)
print(response.text)

"""
Origin: 声明资源的起始位置
User-Agent: 浏览器的身份标识
Host: 服务器的域名
Referer: 防盗链

Cookies: 用户身份标识 <能不加啊就不加>, 
"""
