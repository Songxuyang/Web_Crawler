import re

string = 'PythonahsdgjasghPythonasdjajsk'

# re.match  匹配字符串中首字符<头部>, 只能找一次数据, 假如字符串中首字符没有我们要查找的内容, 就会报错
# re.match 如果匹配到了数据, 返回的是一个对象
# group() 在对象当中取数据
result = re.match('Python', string)
print(result)
print(result.group())
