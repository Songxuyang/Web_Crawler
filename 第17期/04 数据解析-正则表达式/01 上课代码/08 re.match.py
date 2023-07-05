import re


string = 'PythonahsdgjasghPythonasdjajsk'

# re.match  匹配字符串中第一个内容, 如果字符串的最前面没有你要查找的内容就会报错, 只会找头部
# result    得到的结果是一个对象, 用group()在对象中把数据取出来
result = re.match('Python', string)
print(result)

print(result.group())