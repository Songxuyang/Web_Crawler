text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主

收起回复8楼2018-07-04 16:20

RAVV2017: 已发送，麻烦请查收，谢谢
2018-7-4 16:23回复
我也说一句

该来的总会来
物联博士5
1459543548@qq.com
谢谢谢谢

回复9楼2018-07-04 17:18来自Android客户端
BLACKPINK_罗捷
深入物联2
1228074244@qq.com
"""
import re

"""
.       在默认情况下, 匹配除了换行符以外的任意字符
re.S    模式匹配, 能够让 . 匹配到换行符
"""
result = re.findall('Super劫Zed: .................', text, re.S)
# print(result)


"""
\d      匹配一个数字字符
\D      匹配一个非数字字符
"""
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d', text, re.S)
# print(result)

result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\D', text, re.S)
# print(result)


"""
\s      匹配一个空白字符
\S      匹配一个非空白字符
"""
result = re.findall('\s1', text, re.S)
# print(result)
# result = re.findall('\S', text, re.S)
# print(result)

"""
\w      匹配一个单词字符 a-z、A-Z、0-9、_ 文字
\W      匹配一个非单词字符 符号, 空白字符

"""
result = re.findall('\w', text, re.S)
# print(result)
result = re.findall('\W', text, re.S)
# print(result)

"""
+   匹配一个字符的一次或者多次 (最少要有一次出现)
*   匹配一个字符的零次或者多次 (最少可以是零次出现)

.+  匹配一次或者多次
.*  匹配零次或者多次
"""
result = re.findall('Super劫Zed: \d*\D*', text, re.S)
# print(result)
result = re.findall('Super劫Zed: \d+\D+', text, re.S)
# print(result)


result = re.findall('Super劫Zed: \s*', text, re.S)
print(result)
result = re.findall('Super劫Zed: \s+', text, re.S)
print(result)




