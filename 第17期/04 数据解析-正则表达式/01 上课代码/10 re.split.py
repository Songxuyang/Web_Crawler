import re

"""
pattern     匹配规则
string      匹配的字符串
maxsplit    最大分割次数
flags       匹配模式
"""
string = 'Pythonasdkjasd 464654 adhuiaghsdk 564654 akjsdhkashdkja'

result = re.split('\d+', string)
print(result)

result = re.split('\d+', string, maxsplit=1)
print(result)