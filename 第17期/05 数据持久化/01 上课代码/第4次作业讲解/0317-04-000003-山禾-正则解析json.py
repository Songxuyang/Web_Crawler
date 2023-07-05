"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		fmplaycnt 播放量

    - 用正则表达式采集
"""
import re

import requests

url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=23&shuaxin_id=16881261110000'
headers = {
    'Cookie': 'BIDUPSID=A8D9EA340531252B16551CBD43A8D395; PSTM=1681976911; BAIDUID=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; H_WISE_SIDS=131862_114552_216844_213346_214803_219942_110085_243887_244712_249892_256348_256447_256739_254317_257586_257996_258372_258375_230288_259102_259287_258772_234207_234295_253022_260335_260806_259299_253631_261575_261718_261459_261983_259782_260440_261793_259629_236312_262490_262452_261869_262607_262677_262597_262604_249411_259519_259948_262743_262746_262913_263190_256998_263221_263306_263279_243615_263343_261683_263434_254299_261411_263584_257289_262439_262533_263644_262408_262910_257169_262289_263906_263363_256419_264175_264089_264228_257442_256225_262260_255224_264018_264368_259558_256083_264383_264423_264452_264285_256152_264626_264246_258698_264749_261934_264820_264136_261035_261663; ZFY=CMMricp5SfogOfi1RswFaP4NBZN6t5zy:Axurblw8al4:C; BAIDUID_BFESS=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=800lag2h0hahag258401000m1i9qvr81p; H_PS_PSSID=36550_38860_38958_38956_38918_38802_38640_26350; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1688126064; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1688126112; ariaDefaultTheme=undefined; ab_sr=1.0.1_MjgyMzZjN2IxMjY5NzIyYzY2ZWQ2NTAzNGQ2YTcwNzRmZDczYjM5NDZiMDdkMGE0YWQyNTQ1YWVjN2YzNzExYmIyMmFlMjcyYzk2YzJjNjMyM2JjMDVhNDE5NDYyNTQ3MTM2MmU5M2Y1NDZlODYyNjg3YzlhODY0OWEwMGFlMzJjMTE5YzI4NDdhZDMyNzQ4MDA1YmYwZTE5YmNhMDkwZA==; reptileData=%7B%22data%22%3A%2287bae13ee8ed99ddf87f67f1f31fdf4ce6014e09f0fe8e757434c4500b3b88612312e5a033baaef9b71a836a58b6f53f35de74fc20152f9f3cb09bab3f2e4594dee3f7002bdc220ab39023b9f7742f316ca7e0e203afad9be69125ddc36dc865%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22b50b7367%22%7D; RT="z=1&dm=baidu.com&si=0ea9a6fe-6353-4f02-829c-8039b1c56a1b&ss=ljiio6p3&sl=2&tt=31r&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=13gd&nu=47t5yjyw&cl=1b5h"',
    'Authority': 'haokan.baidu.com',
    'Referer': 'https://haokan.baidu.com/tab/gaoxiao_new',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
json_data = response.json()
print(json_data)
print(type(json_data))

json_data = str(json_data)

# {'id': '9266673592642073145', 'title': '分手的原因终于找到了，原来是一起挂的同心圆被别人给剪啦！', 'poster_small': 'https://f7.baidu.com/it/u=2557173170,2348383163&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80', 'poster_big': 'https://f7.baidu.com/it/u=2557173170,2348383163&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80', 'poster_pc': 'https://f7.baidu.com/it/u=2557173170,2348383163&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80,f_auto', 'source_name': '就这么搞笑', 'play_url': 'http://vd4.bdstatic.com/mda-pdc4ueypmq7b5isj/cae_h264/1681516229583661512/mda-pdc4ueypmq7b5isj.mp4?v_from_s=hkapp-haokan-nanjing', 'duration': '01:04', 'url': 'https://haokan.hao123.com/v?vid=9266673592642073145&pd=pc&context=', 'show_tag': 0, 'publish_time': '04月13日', 'is_pay_column': 0, 'like': '1', 'comment': '5', 'playcnt': '84', 'fmplaycnt': '84次播放', 'fmplaycnt_2': '84', 'outstand_tag': '', 'previewUrlHttp': 'https://vd4.bdstatic.com/mda-pdc4ueypmq7b5isj/cae_h264/1681516229583661512/mda-pdc4ueypmq7b5isj.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1688128351-0-0-55ae631ce80b6d3563a979677b4e18ef&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&logid=0151184955&vid=9266673592642073145&pt=4&cr=0&sle=1&sl=573&split=501264', 'third_id': '1760852045386443', 'vip': 0, 'author_avatar': 'https://gips0.baidu.com/it/u=3423469398,1093432278&fm=3012&app=3012&autime=1687938807&size=b200,200&fmt=auto'},
# {'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?},
# \{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?\},

result = re.findall("\{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?\},", json_data)
print(result)