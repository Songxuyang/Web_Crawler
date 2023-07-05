
import csv

"""基于字符串文件类型直接读取"""
# with open('data.csv', mode='r', encoding='utf-8') as f:
#     print(f.read())


"""读取返回列表"""
# with open('douban-list.csv', mode='r', encoding='utf-8') as f:
#     csv_read = csv.reader(f)
#     print(csv_read)
#     for i in csv_read:
#         print(i)

"""读取返回字典对象的方法"""
with open('douban-list.csv', mode='r', encoding='utf-8') as f:
    csv_read = csv.DictReader(f)
    print(csv_read)
    for i in csv_read:
        print(i)

