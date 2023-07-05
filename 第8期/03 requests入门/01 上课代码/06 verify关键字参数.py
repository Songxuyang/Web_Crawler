import requests

"""忽略警告"""
# import urllib3
# urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()


url = 'https://data.stats.gov.cn/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


# requests.exceptions.SSLError   网站链接不安全, 没有相关证书
# 默认requests会自动验证证书
# verify  默认为True
response = requests.post(url=url, headers=headers, verify=False)
html_data = response.text
print(html_data)


