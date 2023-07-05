

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
	<p class="top">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel

selector = parsel.Selector(html)

# 只要标签具有 class 属性, 我们就可以用类选择器定位标签
# .  代表提取标签的类属性, 根据类属性定位
# 具有相同类属性的标签都会被提取到
# 类选择器可以通过标签的类属性(class属性), 精确定位到你想要的标签
# 如果class属性的标签中存在空格，那么空格要用.代替，例如<div class="opt mod"> ，那么result = selector.css('.opt.mod').getall()
result = selector.css('.top').getall()
print(result)