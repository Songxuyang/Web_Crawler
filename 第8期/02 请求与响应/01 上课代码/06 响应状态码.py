# https://movie.douban.com/top250

import requests


headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=lDlTVWragaYFBVncmBlLaPC9FxfghgE8ddR27aCHt8rf81lBCh5nanctaSGXccYK&wd=&eqid=c44c40170000a0460000000661e5681d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)

print(response.status_code)  # 查看响应体的状态码

"""
100 - 199   标识服务器已经接受到了请求
200 - 299   标识请求成功 <200>  <204>
300 - 399   重定向(你要请求的地址, 已经移动到了另外一个位置)
400 - 499   请求地址有误, 在服务器中拿不到数据 <404> <405>
500 - 599   服务器内部错误, 是服务器的问题
"""
