"""
将上课的案例-爬取小说完善。爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
import re
import os
import requests


if not os.path.exists('剑来'):  # 如果没有剑来这个文件夹
    os.mkdir('剑来')

for page in range(1, 11): # 123456789 10

    response = requests.get(f'https://www.bige7.com/book/1031/{page}.html')  # 每一次循环任务, 地址都会变
    html_data = response.text

    """
    <div id="chaptercontent".*?>(.*?)<p class="readinline">.*?</p></div>
    """
    # 解析标题, 作为文件名
    # <h1 class="wap_none">(.*?)</h1>
    title = re.findall('<h1 class="wap_none">(.*?)</h1>', html_data, re.S)[0] + '.txt'
    print(title)

    result = re.findall('<div id="chaptercontent".*?>(.*?)<p class="readinline">.*?</p></div>', html_data, re.S)


    contend = result[0].replace('\u3000\u3000', '').replace('<br /><br />', '\n')

    with open('剑来\\' + title, mode='w', encoding='utf-8') as f:
        f.write(contend)



