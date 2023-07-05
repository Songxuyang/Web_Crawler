

text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360456789@qq.com
Super劫Zed: 0123456789@qq.com
Super劫Zed: 987654321456789@qq.com
Super劫Zed: 4789@qq.com
2018-8-8 16:00回复
我也说一句

"""
import re

# {起始值,结束值} --> 闭区间  标识数量词: 指定范围匹配前一个字符出现的次数
result = re.findall('[1-9][1-9]{5,12}@qq.com', text, re.S)
print(result)