import requests
import re  # 正则表达式的模块, 内置


# 找到了地址后请求地址数据
response = requests.get('https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4')
# 图片数据
data = response.content  # content 是从response对象里面提取二进制数据

# 保存
with open('myvideo.mp4', mode='wb') as f:
    f.write(data)






