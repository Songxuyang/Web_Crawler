"""
	目标地址：https://m.maoyan.com/asgard/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""
import requests

headers = {
    'Cookie': 'iuuid=F5783590DF7F11ED9B25CD5E5234694FA2DAA684142046EEA9F6AB456B2AFF02; _lxsdk_cuid=1879ededf23c8-0483e83e302f2e-26031b51-1fa400-1879ededf23c8; _lxsdk=F5783590DF7F11ED9B25CD5E5234694FA2DAA684142046EEA9F6AB456B2AFF02; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; ci=70%2C%E9%95%BF%E6%B2%99; ci.sig=6ddYdqOybjnPiJJMwTWmS44rF4o; _lxsdk_s=188ddc29cb4-793-726-aed%7C%7CNaN; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1687347699; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1687347699',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# headers=headers  在请求的时候携带请求头伪装
response = requests.get('https://m.maoyan.com/asgard/board/4', headers=headers)
response.encoding = response.apparent_encoding
print(response.text)

"""
User-Agent: 浏览器的身份标识
Host: 访问服务器的域名
referer: 防盗链,告诉服务器此次请求是从哪个页面跳转过来的
origin: 资源地址的地址位置
cookies: 用户身份字段
"""