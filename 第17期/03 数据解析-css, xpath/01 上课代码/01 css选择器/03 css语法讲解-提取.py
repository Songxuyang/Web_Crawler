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
	<p class="top">标签选择器、类选择器、ID选择器</p>
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
# :: 表示属性选择器, 当你提取到标签之后, 需要对标签特定的值进行提取(标签包含的文本内容, 标签的属性)
result = selector.css('a::text').getall()
print(result)

# ::attr(href)      根据标签中包含的属性名字提取属性值
# href              a标签属性的名字
result = selector.css('a::attr(href)').getall()
print(result)
