import re

"""
pattern:    正则语法
repl:       需要替换的字符串; <替换的结果可以是字符串, 也可以是函数>
string:     在哪里匹配数据
count:      指定替换的次数
flags:      匹配模式
"""

string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'


def fun(string):
    return 'python'


# fun 如果传的是一个函数名字, 在sub会默认调用
result = re.sub('Java', fun, string, flags=re.S)
print(result)
