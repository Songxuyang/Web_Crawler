# 简化的html标签, 代表我们请求到的html数据
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>标签选择器</title>
</head>
<style>
	p{
		color: #f00;
		font-size: 16px;
	}
</style>
<body>
	<p>css标签选择器的介绍</p>
	<p>标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel  # 数据解析模块, 封装了css选择器\xpath\re模块

# 1. 把 html 转换成一个对象
selector = parsel.Selector(html)
# print(selector)

# 在css() 括号里面以字符串形式编辑css语法
# span  使用标签选择器提取标签, 直接给标签的名字

# get() 从 selector 对象中提取满足css语法的第一个标签, 有且仅返回第一个, 返回字符串
# getall() 从 selector 对象中提取满足css语法的所有标签, 返回一个列表
result = selector.css('p').getall()
print(result)


