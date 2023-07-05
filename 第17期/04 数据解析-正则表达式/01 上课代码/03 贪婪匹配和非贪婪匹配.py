text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 254551236@qq.com
Super劫Zed: 654545454@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。
"""

import re

result = re.findall('Super劫Zed: \d+@qq.com', text, re.S)
print(result)


"""
贪婪匹配: 默认匹配模式, 会尽可能的在满足规则的前提下, 多匹配数据

?  匹配1次或者0次

.*   匹配除了换行符以外的任意字符, 默认是贪婪模式
.*?  非贪婪匹配, 在符合规则的前提下, 匹配一次返回一次
"""

result = re.findall('Super劫Zed: .*@qq.com', text)
print(result)
result = re.findall('Super劫Zed: .*?@qq.com', text, re.S)
print(result)
