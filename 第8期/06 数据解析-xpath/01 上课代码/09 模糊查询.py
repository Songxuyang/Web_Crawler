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
                
                <li class="pwd-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""
import parsel

selector = parsel.Selector(html_str)


# 模糊查询 <了解>
result = selector.xpath('//li[contains(@class,"it")]').getall()  # 列表取值  \|
print(result)

"""
    xpath语法中:
    []  
        1.用于标签的精确定位
        2.在同级标签中, 可以取第几个, 类似于索引, 索引从1开始
"""


