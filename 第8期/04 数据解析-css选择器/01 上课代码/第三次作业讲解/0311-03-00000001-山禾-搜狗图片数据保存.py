"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
import pprint
import requests
requests.packages.urllib3.disable_warnings()

url = 'https://pic.sogou.com/napi/pc/searchList' # ?

def get_params(page):
    params = {
        'mode': '1',
        'start': str(page),
        'xml_len': '48',
        'query': '风景'
    }
    return params

file_num = 0  # int

for page in range(0, 97, 48):
    print('============================================================\n')
    params = get_params(page)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # pprint.pprint(json_data)

    data_list = json_data['data']['items']
    # print(data_list)
    for data in data_list:
        picUrl = data['picUrl']
        # print(picUrl)

        file_name = str(file_num) + '.jpg'  # 准备好的文件名
        # print(file_name)

        # 保存数据
        try:
            img_data = requests.get(url=picUrl, verify=False, timeout=3).content  # 请求图片数据

            with open('img\\' +  file_name, mode='wb') as f:
                f.write(img_data)
                print('保存完成: ', file_name)
        except Exception as e:
            continue

        file_num += 1



