text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 54077@qq.com
Super劫Zed: 254551@qq.com
Super劫Zed: 6545454@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。
"""

import re


result = re.findall('Super劫Zed: \d{5}@qq.com', text, re.S)
print(result)

result = re.findall('Super劫Zed: \d{6}@qq.com', text, re.S)
print(result)

# {start,stop}  表示数量词, 限制前一个字符的匹配数量, 闭区间
result = re.findall('Super劫Zed: \d{5,6}@qq.com', text, re.S)
print(result)
