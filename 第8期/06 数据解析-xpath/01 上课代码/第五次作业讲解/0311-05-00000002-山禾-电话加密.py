
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

tel = "18189895458"

import re

def func(temp):  # 必须得有一个参数,
    # print(temp)  # ---> 对象
    res = temp.group()
    # print(res)
    res_2 = res[:3] + '****' + res[-4:]
    # print(res_2)
    return res_2

# func 函数是 sub() 默认会调用的函数, 函数 return 返回的结果就是最终替换的结果
result = re.sub('\d{11}', func, tel)
# print(result)

result2 = re.sub('\d{11}', lambda x:x.group()[:3] + "****" + x.group()[-4:], tel)
print(result)

