import requests

response = requests.get(f'https://www.bige7.com/book/1031/1.html')
"""
https://www.bige7.com/book/1031/1.html

https://            请求协议的类型<http/https>, 超文本传输协议<文字/图片/视频/音频>
www                 请求服务器的名字  www <world wide web> 万维网  mail<邮箱服务器的名字>
bige7.com           域名,  bige7.com.cn.net   cn是一级域名  com 是二级域名
/                   域名后面的第一个 /  代表服务器的根路径
book/1031/1.html    资源位置, 类似于文件的盘符路径
"""