text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com 785---310@qq.com 416648946@qq.com
2018-8-8 16:00回复
我也说一句
"""
import re

"""
贪婪匹配: 默认匹配的模式, 只要满足正则规则的数据, 会尽可能多的匹配 <数据长度就会很长>

.*      匹配除了韩航服意外的任意字符, 默认是贪婪模式
.*?     使用非贪婪模式匹配, 匹配一次返回一次
?       匹配1次或者0次
"""

result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
print(result)

"""
Super劫Zed: 540775360@qq.com.*?Super劫Zed: 785462310@qq.com
Super劫Zed: 416648946@qq.com
"""
result = re.findall(' .*?@qq.com', text, re.S)
print(result)





