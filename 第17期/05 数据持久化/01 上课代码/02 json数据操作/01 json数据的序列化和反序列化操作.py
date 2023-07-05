import json  # 内置

# []  {}
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

"""
json序列化: 将对象转化成json字符串
dumps()     序列化json字符串
"""
json_str = json.dumps(data)
print(json_str)
print(type(json_str))


"""
json反序列化: 将json字符串转化成对象
dumps()     序列化json字符串
"""
json_obj = json.loads(json_str)
print(json_obj)
print(type(json_obj))

