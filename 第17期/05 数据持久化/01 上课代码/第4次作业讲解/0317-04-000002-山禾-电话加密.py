
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458

    请用正则表达式解决
"""
import re

# def func(x):
#     # print(x)
#     str_ = x.group()
#     return str_[:3] + '****' + str_[-4:]
#
# tel = "18123115458"

#
#
# result = re.sub('\d{11}', func, tel)
# print(result)


# tel = "18123115458"
# result = re.sub('\d{11}', lambda x:x.group()[:3] + '****' + x.group()[-4:], tel)
# print(result)


tel = "18123115458"
# 分组匹配
# (\d{3}) 分组一  (\d{4}) 分组二  (\d{4}) 分组三
# \\1 取分组一
result = re.sub('(\d{3})(\d{4})(\d{4})', '\\1****\\3', tel)
print(result)
