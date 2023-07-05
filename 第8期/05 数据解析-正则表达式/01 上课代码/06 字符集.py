

text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360456789@qq.com
Super劫Zed: 123456789@qq.com
Super劫Zed: 987654321456789@qq.com
2018-8-8 16:00回复
我也说一句

"""
import re


# []  代表字符集, 作用: 收集需要提取的字符串
# 一个 [] 只能匹配一个数字
result = re.findall('[0-9]*@qq.com', text, re.S)
print(result)


result = re.findall('[0-9]*@qq.com', text, re.S)
print(result)