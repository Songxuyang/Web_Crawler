

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
	<p>标签</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel  # 数据解析模块, 封装了css选择器\xpath\re模块


selector = parsel.Selector(html)

#  : 标识伪类选择器
# nth-child  从前往后数, 要取第几个, 3是索引, 从1开始
result = selector.css('p:nth-child(2)').get()
print(result)

