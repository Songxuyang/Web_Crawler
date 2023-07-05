import requests


response = requests.get('https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=72')

"""
https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=72

https://        请求协议类型
www             服务器名字  www(world wide web) 万维网; mail(邮箱服务器名字)
ku6.com         服务器域名
/               服务器根目录
video/feed?pageNo=0&pageSize=40&subjectId=72   资源路径

url地址/连接地址/api地址/api接口
"""



