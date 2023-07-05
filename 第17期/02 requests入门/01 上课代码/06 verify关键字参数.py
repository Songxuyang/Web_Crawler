import requests
# urllib3.disable_warnings()  # 忽略关闭认证ca证书之后引发的警告
requests.packages.urllib3.disable_warnings()



url = 'https://data.stats.gov.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# verify=False  使用requests模块发送请求的时候,不验证ca证书,默认会验证(verify=True)
response = requests.post(url=url, headers=headers, verify=False)
data = response.text
print(data)

"""
网站没有证书使用requests模块请求会报错 --> requests.exceptions.SSLError
"""
