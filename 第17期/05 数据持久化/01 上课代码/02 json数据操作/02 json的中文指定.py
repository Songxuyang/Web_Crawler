import json

data = {
    'name': '青灯',
    'shares': 100,
    'price': 542.23
}

# json字符串默认使用unicode编码, 无法显示中文
# ensure_ascii=False  不适用默认编码

json_str = json.dumps(data, ensure_ascii=False)
with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

