"""
	目标地址：https://m.maoyan.com/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""
import requests

url = 'https://m.maoyan.com/board/4'

headers = {
    # 'Cookie': 'uuid_n_v=v1; iuuid=BDAB8D50791A11EC8741DBA2CF60E163B1A8687D291B4069B1D01A6E824A0D3B; webp=true; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1642591631; _last_page=undefined; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1642592204',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)

"""
User-Agent: 浏览器的身份标识
Host: 想访问的服务器的域名地址
Referer: 防盗链, 你是从哪里过来的
Origin: 服务器的根路经
Cookies: 用户身份的标识

请求头字段, 可能会加密<可能会看到 (sign: fhesfhkeshfisaehnkldf)>
"""
