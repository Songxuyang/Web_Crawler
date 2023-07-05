'''
split():
    分割字符串 去掉了匹配到的字符串
    结果是列表形式
    maxsplit: 默认是0 表示全部切割
                1 代表切割一次
                2 代表切割两次
'''

import re


pattern = '\d+'
string = 'Pythonasdkjas 464654 adhuiaghsdk 564654 akjsdhkashdkja'
result = re.split(pattern, string, 10)
print(result)