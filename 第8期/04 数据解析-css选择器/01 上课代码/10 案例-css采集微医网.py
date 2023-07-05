import requests
import parsel


# 1. 找数据的地址
url = 'https://www.guahao.com/expert/61409/%E5%86%85%E7%A7%91'

# 2. 请求数据
response = requests.get(url=url)
html_data = response.text
# print(html_data)

# 3. 数据解析
selector = parsel.Selector(html_data)
lis = selector.css('.g-doctor-item')

for li in lis:
    doctor_name = li.css('dl dt a::attr(title)').get()
    doctor_level = li.css('dl dt::text').getall()[1].strip()
    doctor_kind = li.css('dd p:nth-child(1)::text').get()
    doctor_belongin = li.css('.g-txt-ell::text').get()
    doctor_score = li.css('.star em::text').get()
    doctor_wenzhen = li.css('.star-count span:nth-child(2) i::text').get()
    doctor_skill = li.css('.skill p::text').get().strip().replace(' ', '').replace('\n', '')
    doctor_pic_price = li.css('.infos.image span em:nth-child(2)::text').get().strip()
    doctor_video_price = li.css('.infos.video span em:nth-child(3)::text').get()

    if doctor_video_price:
        doctor_video_price = doctor_video_price.strip()

    # 数据解析的语法没有解析到数据, 会返回 None, 没有 strip() 方法
    print(doctor_video_price)

