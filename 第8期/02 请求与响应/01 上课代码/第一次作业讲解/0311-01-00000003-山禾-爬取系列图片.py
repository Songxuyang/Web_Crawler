"""
上课爬取图片的案例

	课上讲解是的爬取 香气四溢的薯条 (1/10) 这个系列图片,
	这个系列一共十张, 要求大家一次性将一个系列图片全部爬取下来

	地址： https://www.hexuexiao.cn/a/124525.html

请下下方开始编写代码
"""
import requests
import re  # 正则表达式的模块, 内置


for page in range(10):
    # 找到了地址后请求地址数据
    response = requests.get(f'https://www.hexuexiao.cn/a/124525-{page}.html')
    html_data = response.text
    print(html_data)

    # 解析图片的地址

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










