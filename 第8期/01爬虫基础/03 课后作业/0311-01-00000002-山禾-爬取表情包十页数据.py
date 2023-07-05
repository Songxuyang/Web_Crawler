"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
"""请下下方开始编写代码"""

import requests
import re
for page in range(1,11):
    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(str(page))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # print(response.text)

    title = re.findall('<a href="/biaoqing/detail/id/.*?.html" title="(.*?)">', response.text, re.S)
    # print(title)
    result = re.findall('<img class="ui image lazy" data-original="(.*?)"', response.text, re.S)
    # print(result)

    # print(len(title), len(result))
    i = 0
    for url in result:
        response = requests.get(url, headers=headers)
        data = response.content
        tip = result[i].split('.')[-1]
        new_title = title[i].replace('?', '').replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('"', '').replace('|', '').replace('<', '').replace('>', '')
        with open('./作业2/{}.{}'.format(new_title, tip), 'wb') as f:
            f.write(data)
            i += 1

    print('=========第{}页爬取完毕========='.format(page))

