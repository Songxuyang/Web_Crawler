"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
"""请下下方开始编写代码"""
import re
import os
import requests


response = requests.get('https://fabiaoqing.com/biaoqing')
html_data = response.text
# print(html_data)

"""
<img class="ui image lazy" data-original="(.*?)" src=".*?".*?</a>

"""

result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=".*?".*?</a>', html_data, re.S)
# print(result)


for img_url in result:
    response2 = requests.get(img_url)  # 响应体  图片, 视频, 音频都是属于二进制数据

    # 图片数据
    data = response2.content  # content 是从response对象里面提取二进制数据
    # print(data)

    # 保存图片的文件名
    file_name = img_url.split('/')[-1]
    # print(file_name)

    # 保存
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('保存完成:', file_name)

