import requests
import re  # 正则表达式的模块, 内置


# 找到了地址后请求地址数据
response = requests.get('https://www.hexuexiao.cn/a/124525-0.html')
html_data = response.text
print(html_data)

# 解析图片的地址
"""
# 元素面板复制的
<a class="btn btn-default btn-xs" href="https://i.hexuexiao.cn/up/da/75/47/f59543039ce27d69ef5d25b5a04775da.jpg.source.jpg" role="button" target="_blank">
                            <i class="fa fa-download" style="color: #999;"></i> 下载本图
                        </a>
                        
<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">.*?

# 终端复制的结果
<a class="btn btn-default btn-xs" href="https://i.hexuexiao.cn/up/da/75/47/f59543039ce27d69ef5d25b5a04775da.jpg.source.jpg" role="button" target="_blank">

# 元素面板复制的标签, 和请求到终端复制的数据有出入**<重点>
# 一切数据解析以代码终端获取的数据为准

"""
result = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">.*?', html_data, re.S)
print(result)


# 取图片链接
img_url = result[0]
print(img_url)

# 请求图片地址
response2 = requests.get(img_url)  # 响应体  图片, 视频, 音频都是属于二进制数据

# 图片数据
data = response2.content  # content 是从response对象里面提取二进制数据
# print(data)

# 保存图片的文件名
file_name = img_url.split('/')[-1]
print(file_name)

# 保存
with open(file_name, mode='wb') as f:
    f.write(data)






