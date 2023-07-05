import re

"""
pattern    匹配规则 
repl       匹配到的数据需要替换成什么--> (可以是字符串, 也可以是函数规则)
string     在哪里匹配
count      替换次数
flags      匹配模式
"""

string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'
# 字符串的替换方法
result = re.sub('Java', 'python牛逼', string)
print(result)

result = re.sub('Java', 'python牛逼', string, count=1)
print(result)

def func(x):
    print('匹配到的数据会放到此参数当中来:', x.group())
    return x.group().replace('a', '@')

result = re.sub('Java', func, string, count=1)
print(result)


# re.finditer()