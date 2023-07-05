"""
时间戳: 格林威治时间1970年1月1日0时0分0秒开始 到 目前 位置所消耗的时间数
    秒级时间戳: 10为数字
    毫秒级时间戳: 13为数字
    微秒级时间戳: 16为数字
"""
import time

import requests


def get_time():
    """获取时间戳的函数"""
    now_time = str(int(time.time() * 1000))
    print('当前时间戳为:', now_time)
    return now_time

cookies = {'seesion': 'vnrasebgvi'}

# 创建一个会话位置对象
session = requests.Session()

"""请求验证码, 保存"""
img_time = get_time()
img_url = 'http://118.126.88.143:5000/login/captcha?image_code=' + img_time
print('图片地址:', img_url)

# 使用回话维持对象发送请求
img_response = session.get(url=img_url, cookies=cookies).content
with open('yzm.png', mode='wb') as f:
    f.write(img_response)

# 手动识别验证码
img_code = input('请输入验证码:')
print('您输入的验证码为:', img_code)

"""构建登录请求"""
login_url = 'http://118.126.88.143:5000/api/private/v1/login'
json_data = {
    "image_code": img_time,
    "username": "admin",
    "password": "123456",
    "captcha_code": img_code  # 手动验证码
}

# 使用回话维持对象维持用户的登录状态
login_response = session.post(url=login_url, json=json_data)
print(login_response.cookies.get_dict())
print(login_response.json())


# 其他网站构建请求联系, 一般是通过cookies字段