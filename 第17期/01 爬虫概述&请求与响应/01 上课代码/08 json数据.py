
"""json数据"""

# json数据是目前主流的数据交换格式 (结构清晰, 方便取值)
# 形式:  外层 {}  []  包裹  嵌套数据
# {"字段1": "值1",字段2: {嵌套字段1: 嵌套字段值1}, {}, {} ...}
# json数据和字典非常像, 但是有区别, 引号, json数据必须用双引号


"""
在json数据中, 值必须是以下数据类型

字符串
数字
对象(json对象)<嵌套形式>
数组
布尔值
null --> 字符串
"""
import requests


response = requests.get('https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=72')
print(response.json())

# # 通过 json() 提取json数据之后, 会在底层经过数据转换, 转换成一个对象
print(type(response.json()))
