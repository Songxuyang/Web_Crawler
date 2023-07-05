# https://movie.douban.com/top250

import requests


headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://www.baidu.com/link?url=lDlTVWragaYFBVncmBlLaPC9FxfghgE8ddR27aCHt8rf81lBCh5nanctaSGXccYK&wd=&eqid=c44c40170000a0460000000661e5681d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)

print(response.text)  # 获取响应体的文本数据  --> str  --> html
print(response.content)  # 获取响应体的二进制数据  --> str
# print(response.json())  # 获取响应体的json数据, 如果不是json数据. 使用json()提取会报错(json.decoder.JSONDecodeError)
print(response.headers)  # 查看响应头数据
print(response.encoding)  # 指定响应体编码
print(response.apparent_encoding)  # 自动识别响应体编码
print(response.cookies)  # 获取响应体的cookies字段信息, 得到的是一个 RequestsCookieJar对象
print(response.cookies.get_dict())  # RequestsCookieJar 对象转换成字典
print(response.url)  # 查看响应体的地址
print(response.status_code)  # 查看响应体的状态码
