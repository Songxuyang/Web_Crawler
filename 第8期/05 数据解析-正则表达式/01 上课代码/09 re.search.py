import re

string = '00PythonahsdgjasghPythonasdjajsk'

# re.search  在字符串中任意位置查找字符串, 只能找一次数据,
# re.search 如果匹配到了数据, 返回的是一个对象
# group() 在对象当中取数据
result = re.search('Python', string)
print(result)
print(result.group())
