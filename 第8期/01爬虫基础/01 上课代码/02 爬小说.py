import requests
import re  # 正则表达式的模块, 内置


# 找到了地址后请求地址数据
response = requests.get('https://www.bige7.com/book/1031/1.html')
html_data = response.text

# 数据解析
# 正则表达式
# 不要的数据用  --> .*?站位
# 需要的数据用  --> (.*?)站位
"""
<div id="chaptercontent".*?>(.*?)<p class="readinline">.*?</p></div>
"""
result = re.findall('<div id="chaptercontent".*?>(.*?)<p class="readinline">.*?</p></div>', html_data, re.S)
print(result)
print(len(result))

contend = result[0].replace('\u3000\u3000', '').replace('<br /><br />', '\n')

with open('a.txt', mode='w', encoding='utf-8') as f:
    f.write(contend)





