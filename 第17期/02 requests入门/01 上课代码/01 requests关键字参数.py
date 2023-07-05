import requests

headers = {
    'Cookie': 'iuuid=F5783590DF7F11ED9B25CD5E5234694FA2DAA684142046EEA9F6AB456B2AFF02; _lxsdk_cuid=1879ededf23c8-0483e83e302f2e-26031b51-1fa400-1879ededf23c8; _lxsdk=F5783590DF7F11ED9B25CD5E5234694FA2DAA684142046EEA9F6AB456B2AFF02; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; _lxsdk_s=188ddc29cb4-793-726-aed%7C%7CNaN; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1687347699; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1687347699',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.get(url='https://m.maoyan.com/asgard/board/4', headers=headers)
print(response.url)

"""
method: 请求方法  get post
url: 请求网址的关键字

params: (可选参数) 指定查询参数
data: (可选参数) 指定请求参数
json: (可选参数) 指定json数据形式发送请求

headers: (可选参数) 请求头关键字参数
cookies: (可选参数) 请求的时候指定用户身份标识
proxies: (可选参数) 使用代理请求的关键字

timeout: (可选参数) 指定请求的时间, 单位/秒
allow_redirects: (可选参数) 是否允许重定向, 300左右
verify: (可选参数) 控制是否验证网站证书

files: (可选参数) 上传文件
auth: (可选参数) 权限认证
stream: (可选参数) 是否是数据流传输的数据
"""