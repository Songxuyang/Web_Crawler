


"""json数据"""
"""
目前网络主流的数据传递格式 (结构清晰, 取值方便)
    形式: 
        外层 {} []
            {字段1: 值1, 字段2:[{嵌套字段1: 嵌套字段1的值}, {}, {} ...]}
        内层: 嵌套, 包裹数据
        字段与值只能用双引号包裹
        json数据类型: 字符串
        
        在json数据中, 所有字段的值必须是以下类型:
            字符串
            数字
            对象<列表, 字典>
            布尔值
            null  空的意思, None
    
    和字典的形式非常像, <键和值可以用双引号, 也可以用单引号>
    对象

"""

import requests


response = requests.get('https://pvp.qq.com/web201605/js/herolist.json')
print(response.json())
# print(response.text)
print(type(response.json()))  # 底层自动把字符串类型的json数据, 转换成对象


