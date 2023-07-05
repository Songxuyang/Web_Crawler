import parsel
import requests

url = 'https://www.guahao.com/expert/61409/%E5%86%85%E7%A7%91'
response = requests.get(url=url)
html_data = response.text
# 在解析数据前， 一定要打印查看数据是请求到了
# print(html_data)

selector = parsel.Selector(html_data)
lis = selector.css('.g-doctor-items.to-margin>ul>li')

for li in lis:
    doctor_name = li.css('.wrap>a::text').get()
    doctor_level = li.css('dl>dt::text').getall()[1].strip()
    doctor_kind = li.css('dd>p:nth-child(1)::text').get()
    doctor_Belonging = li.css('dd>p:nth-child(2)>span::text').get()
    doctor_score = li.css('.star>em::text').get()
    doctor_inquiry = li.css('.star-count>span:nth-child(2)>i::text').get()

    doctor_goodFor = li.css('.skill>p::text').get().strip().replace('\n', '').replace(' ', '')

    result = li.css('.star-count>span:nth-child(1)::text').get()

    print(result)
