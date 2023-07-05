# https://movie.douban.com/top250

import requests


headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=lDlTVWragaYFBVncmBlLaPC9FxfghgE8ddR27aCHt8rf81lBCh5nanctaSGXccYK&wd=&eqid=c44c40170000a0460000000661e5681d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)

# response.request  查看请求体信息
print(response.request.url)  # 查看请求体中url地址
print(response.request.headers)  # 查看请求体请求头字段
print(response.request.method)  # 查看请求体请求方法
