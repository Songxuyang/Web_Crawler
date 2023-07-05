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
我也说一句_
"""

import re

# 默认情况下一个元字符只能匹配到一个字符串

"""
. 在默认情况下, 可以匹配除了换行符以外的任意字符
re.S 匹配模式, 能够让 . 匹配到换行符
"""
# 在元字符的前后加字符串的约束, 那么匹配的数据也要满足约束条件
# 如果有字符串即满足约束条件也满足元字符规则, 那么就会被匹配到
# 如果没有字符串满足正则表达式规则, 那么就会返回空列表
result = re.findall('Super劫Zed: .................', text, re.S)
print(result)

"""
\d  匹配一个数字字符
\D  匹配一个非数字字符
"""
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d', text)
print(result)
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\D\D\D\D\D\D\D', text)
print(result)


"""
\s  匹配一个空白字符(换行,空格,\t, tab键)
\S  匹配一个非空白字符
"""
result = re.findall('\s', text)
print(result)

result = re.findall('\S', text)
print(result)

"""
\w  匹配一个单词字符, 即a-z、A-Z、0-9、_、包括各个国家语言文字
\W  匹配一个非单词字符
"""
result = re.findall('\w', text)
print(result)

result = re.findall('\W', text)
print(result)

"""
+  匹配前一个字符一次或者多次(最少要出现一次)
*  匹配前一个字符零次或者多次(最少可以是零次)

.+  匹配一次或者多次
.*  匹配零次或者多次
"""
result = re.findall('Super劫Zed: .\d+', text)
print(result)
result = re.findall('Super劫Zed: \d*\D*', text)
print(result)


# result = re.findall('Super劫Zed: \s+', text)
# print(result)
# result = re.findall('Super劫Zed: \s*', text)
# print(result)

