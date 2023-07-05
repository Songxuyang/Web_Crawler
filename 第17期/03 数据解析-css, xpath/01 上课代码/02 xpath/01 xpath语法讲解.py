html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 
                
                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li> 
                
                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 
                
                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 
                
                <li class="item-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""

import parsel


# # 转换数据类型, 能够把缺失的html标签补充完整
selector = parsel.Selector(html_str)
# print(selector)
# # selector.xpath()

"""根节点的使用"""
result = selector.xpath('/html/body/div/ul/li/a').getall()
print(result)

"""
    xpath语法规则中
    /   表示从根节点开始提取(用得少),还表示取下一级标签
    如果你打算从根节点提取, 那么必须从html这个节点开始提取

"""
print('-' * 100 + '\n')


"""跨节点的使用"""
result2 = selector.xpath('//a').getall()
result3 = selector.xpath('/html//a').getall()
print(result2)
print(result3)

"""
    xpath语法规则中(用的极多)
    //   表示跨节点提取, 而不用考虑节点位置
"""
print('-' * 100 + '\n')

"""选取当前节点"""
# 选中<ul>标签, 然后提取<ul>标签下面所有的<li>标签
result = selector.xpath('//ul')
result4 = result.xpath('./li').getall()
print(result4)
"""
    xpath语法规则中
    .   表示取当前节点
    使用场景: 需要对选取的标签进行二次提取的时候,需要用到 .
"""
print('-' * 100 + '\n')

"""选取当前节点的父节点"""
# 选取<a>节点的父节点
result = selector.xpath('//a')
result5 = result.xpath('..').getall()
print(result5)
"""
    xpath语法规则中
    ..   表示取当前节点的父节点(用的极少)
"""
print('-' * 100 + '\n')

"""@属性定位和属性取值"""
# 获取第四个<a>标签, 并获取其href属性值
result = selector.xpath('//a[@href="link4.html"]').getall()
print(result)

result = selector.xpath('//a[@href="link4.html"]/@href').getall()
print(result)
"""
    xpath语法规则中
    @ 有两个用途
    1. 根据标签特有的属性(class,href,src,id,title等等)精确定位到想要的标签    
    2. 可以根据已经定位好的标签, 指定标签内属性的名字, 获取属性值  
"""
print('-' * 100 + '\n')

"""获取标签包含的文本内容"""
# 获取第四个<a>标签, 取其包含的文本内容
result = selector.xpath('//a[@href="link4.html"]/text()').getall()
print(result)
"""
    xpath语法规则中
    text()  作用在于获取指定标签后, 可以提取标签包含的文本内容
"""
print('-' * 100 + '\n')

"""同级标签精确定位"""
# 获取第三个li标签的节点
result = selector.xpath('//li[3]').getall()
print(result)

"""
    xpath语法规则中
    对于获取到的多个标签, 可以用 [] 精确定位获取标签的第几个
    [] 内部填标签的排列的顺序, 类似于索引取值, 索引从1开始
"""
print('-' * 100 + '\n')

"""多条件查询"""
# 获取所有<li>标签的属性值和<a>标签包含的文本, 只能使用一行 xpath 解决
result = selector.xpath('//li/@class|//a/text()').getall()
print(result)
"""
    xpath语法规则中
    |   表示多条件查询, 左右两边分别是两个条件, 满足其中一个条件的标签都会被找到(逻辑或)
    用的不多
"""
print('-' * 100 + '\n')


