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

import parsel  # 数据解析模块, 第三方, pip install parsel

# 1. 转化对象
selector = parsel.Selector(html)  # Selector 就具有一系列数据解析的方法  css/xpath
print(selector)

# 2. 解析数据
"""标签选择器"""
# 所有通过css选择则器解析出来的数据都是一个对象(Selector)
# p  代表根据标签的名字做定位, 叫做标签选择器
# get() 从 Selector 对象中提取第一个数据, 直接返回字符串数据给我们
# result = selector.css('p').get()
# getall() 从 Selector 对象中提取提取所有数据, 返回一个列表
result = selector.css('p').getall()
print(result)

print('-' * 100 + '\n')

"""类选择器"""
# . 代表提取标签的类型(class)
# 具有相同类属性的标签都会被提取
# 类选择器是通过标签的类属性(class属性)精确定位到你想要的标签
result2 = selector.css('.top').getall()
print(result2)

# 如果类属性值是带空格的, 那么空格需要用 . 代替
result3 = selector.css('.top .python').getall()
print(result3)
print('-' * 100 + '\n')

"""ID选择器"""
# '#'  使用 id 选择器提取数据
# contend  代表 id 属性的属性值
# id  在 html中一般是唯一的
result4 = selector.css('#contend').getall()
print(result4)
print('-' * 100 + '\n')

"""组合选择器"""
# 组合选择器主要是加约束
result5 = selector.css('li#res.top').getall()
print(result5)

# 如果使用组合选择器, 标签选择器必须放最前面
result5 = selector.css('li#res.top').getall()
print(result5)
result5 = selector.css('li.top#res').getall()
print(result5)

"""
以上选择器的作用是用于做定位
"""
