# 简化的html标签
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
	<p class="top python">css标签选择器的介绍</p>
	<p class="top python">css标签选择器的介绍333333</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<p class="top">标签选择器、类选择器、ID选择器22222</p>
	<a href="https://www.baidu.com">百度一下</a>
	
	<div id="contend">具有id属性的标签</div>
	
	<span> 我是一个span标签</span>
	
	<li class="top" id="res">组合选择器</li>
	
</body>
</html>
"""

import parsel

# 1. 转化对象
selector = parsel.Selector(html)
print(selector)

# 2. 解析数据
# : 表示伪类选择器
# nth-child 满足标签的第几个元素
# (2) 选择满足标签的第二个元素, 类似索引, 从1开始取
# 伪类主要是在同级标签中定位到指定的第几个
result = selector.css('p:nth-child(2)::text').getall()
print(result)
