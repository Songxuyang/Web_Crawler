# 导入模块
import requests  # 数据请求模块, 第三方模块  pip install requests

# response 响应体, 请求返回的对象
# get 是一种请求方式, post, put , get, delete, options...(get, post)
# https://www.baidu.com/ 请求地址
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

response = requests.get('https://www.ku6.com/detail/76', headers=headers)
print(response)

# 只要是对象就具有对象的属性和方法, 属性没有(),  方法才有括号
# .text  获取response对象的文本内容
print(response.text)
print(type(response.text))


"""
爬虫项目的步骤:
1. 找数据所在的地址(url地址<链接地址>), (数据抓包, 分析网页性质 <静态网页/动态网页> )
2. 请求地址数据< html, js数据, css数据...图片, ...>
3. 数据的解析, 提取咱们需要的数据, 剔除不需要的数据
4. 数据保存<本地文件, 数据库<redis数据库, MongoDB数据库, mysql数据库>>
"""

