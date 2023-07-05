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
	<p class="top" id="contend">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel

selector = parsel.Selector(html)

"""
::  标识属性提取器,
    当我们提取到标签后, 需要获取标签包含的文本内容, 可以用属性提取器
text   提取标签包含的文本内容
"""
result = selector.css('p.top#contend::text').getall()
print(result)

"""
::attr(href)   根据标签中包含的属性名字提取属性的值
href   属性名字
"""
result = selector.css('a::attr(href)').get()
print(result)
