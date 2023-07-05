import requests

response = requests.get('https://i.hexuexiao.cn/up/da/75/47/f59543039ce27d69ef5d25b5a04775da.jpg')
# .content --> 提取响应体二进制数据
img_data = response.content
print(img_data)


# 图片\音频\视频
with open('a.jpg', mode='wb') as f:
    f.write(img_data)