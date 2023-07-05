import requests

url = 'https://m.maoyan.com/board/4'

headers = {
    # 'Cookie': 'uuid_n_v=v1; iuuid=BDAB8D50791A11EC8741DBA2CF60E163B1A8687D291B4069B1D01A6E824A0D3B; webp=true; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1642591631; _last_page=undefined; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1642592204',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
"""
method: 请求方法, 只需要掌握 get post
url: 请求地址<数据对应的网址>

# 反扒处理三件套
headers: (可选的) 请求头字段
cookies: (可选的) 字典, 携带cookies发送请求
proxies: (可选的) ip代理的关键字参数<使用代理伪装>

# 网址参数构建
params: (可选的) 构建查询参数使用的关键字
data: (可选的) 构建请求参数使用的关键字(post请求)
json: (可选的) 在请求的时候参数是json格式, 就用此关键字传递

timeout: (可选的) 设置响应时间, 一旦超过时间, 整个程序报错
allow_redirects: (可选的) 是否允许重定向
verify: (可选的) 网络建站的过程中, ca证书, ssl证书, 默认requests模块请求的时候会自动验证证书

files: (可选的) 文件参数
auth: (可选的) 权限认证
"""

# 异常重试: 通过代码层面解决
