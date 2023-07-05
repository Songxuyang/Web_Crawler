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

selector = parsel.Selector(html_str)

# 选中<a>标签爸爸, 然后取父节点的 class 属性值
# result = selector.xpath('//a')
# result_2 = result.xpath('../@class').getall()
# print(result_2)

# 获取第四个<a>标签
result = selector.xpath('//a[@href="link4.html"]').getall()
print(result)

"""
    xpath语法中
    @ 有两个用途   
        1. 可以根据已经选取的标签, 获取标签指定属性名的值
        2. 根据标签特有的属性<class, href, src, id, title>精确定位标签
"""

