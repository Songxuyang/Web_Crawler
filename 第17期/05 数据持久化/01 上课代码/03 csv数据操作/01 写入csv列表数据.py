"""
csv数据格式:
    每一行是一条数据
    每一行中每个数据字段有分隔符号, 默认为逗号
"""

import csv  # 内置

data = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [5, 6, 7, 8]
]

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    # newline=''  指定数据新行是一个空字符串, 不然保存会有数据空行
    # csv.writer(f)  实例化一个csv数据的写入对象, 括号内部传递文件对象
    csv_write = csv.writer(f)
    for i in data:
        # writerow(i)  把数据一行一行<一条一条>写入, 传入(列表/元组)
        csv_write.writerow(i)
