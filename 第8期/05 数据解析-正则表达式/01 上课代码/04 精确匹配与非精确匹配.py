text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1

收起回复5楼2018-07-04 14:10
Super劫Zed: 416648946@qq.com
Super劫Zed: 111111111@qq.com
Super劫Zed: 222222222@qq.com
2018-8-8 16:00回复
我也说一句
"""
import re

"""
精确匹配: 先根据正则语法匹配数据, 然后提取() 中间的部分
"""

result = re.findall('Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)


# 一次性精匹配多次, 会返回列表嵌套元祖的这样的结构
result = re.findall('Super劫Zed: (.*?)@qq.com\nSuper劫Zed: (.*?)@qq.com', text, re.S)
print(result)







