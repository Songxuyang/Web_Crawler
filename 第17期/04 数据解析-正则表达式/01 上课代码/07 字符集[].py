text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 54077@qq.com
Super劫Zed: 54078@qq.com
Super劫Zed: 254551@qq.com
Super劫Zed: 6545454@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。
"""

import re


# 一个[]只能匹配一个字符串, 只有字符集里面罗列的内容才可以匹配到
result = re.findall('Super劫Zed: [0123456789]*@qq.com', text)
print(result)


result = re.findall('Super劫Zed: [0-9]*@qq.com', text)
print(result)
result = re.findall('Super劫Zed: [a-zA-Z0-9]*@qq.com', text)
print(result)


result = re.findall('[:1]', text)
print(result)

"""
.*?     站位
(.*?)   精确匹配
"""
