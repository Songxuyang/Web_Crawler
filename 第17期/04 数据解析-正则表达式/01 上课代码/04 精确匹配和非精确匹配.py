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

"""
精确匹配: 先根据正则语法规则匹配数据, 然后提取()内的数据部分
()  表示精确匹配
"""

result = re.findall('Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)
