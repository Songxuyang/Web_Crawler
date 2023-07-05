

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

result = selector.css('p.top#contend').getall()
print(result)

# 加约束
# 组合选择器在使用时候, 标签选择器一定要放最前面
result = selector.css('p#contend.top').getall()
print(result)
