import requests  # 数据请求模块 pip install requests


# requests.get 发送一个 https://www.baidu.com/ 的请求
# 服务器接受到请求后会响应数据内容
response = requests.get('https://www.baidu.com/')
# 对象有对象的方法和属性
# .text  获取 Response 对象的文本内容
print(response.text)


"""
爬虫项目实现步骤:
1. 找数据对应的请求地址
    静态网页: 在网页源代码能够找到的数据, 属于静态数据, 对应的地址是当前页面地址导航栏的地址
    动态网页

2. 通过代码发送地址请求
3. 提取需要的数据内容, 剔除不需要的
4. 保存数据
"""

# 知识内容繁琐, 细碎

