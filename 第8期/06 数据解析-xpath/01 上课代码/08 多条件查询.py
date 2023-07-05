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


# 获取所有<li>标签的class属性值, 获取<a>标签包含的文本>, 只能一次匹配
result = selector.xpath('//li/@class|//a/text()|//a/@href').getall()  # 列表取值  \|
print(result)

"""
    xpath语法中:
    []  
        1.用于标签的精确定位
        2.在同级标签中, 可以取第几个, 类似于索引, 索引从1开始
"""


