"""
上课爬取图片的案例

	课上讲解是的爬取 香气四溢的薯条 (1/10) 这个系列图片,
	这个系列一共十张, 要求大家一次性将一个系列图片全部爬取下来

	地址： https://www.hexuexiao.cn/a/124525.html

请下下方开始编写代码
"""

import requests
import re


for page in range(0, 10):
    url = 'https://www.hexuexiao.cn/a/124525-{}.html'.format(str(page))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    title = re.findall('<h1 class="text-center showh3">(.*?)</h1>', response.text, re.S)[0].strip().replace(' ', '').replace('\n', '').replace('/', '_')
    result = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role="button" target="_blank">', response.text, re.S)
    response = requests.get(result[0], headers=headers)
    data = response.content

    with open('./作业3/{}.jpg'.format(title), 'wb') as f:
        f.write(data)

    print('=========已爬取第{}张========='.format(page+1))