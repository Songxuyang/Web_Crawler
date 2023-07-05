import parsel
import requests


def get_one_chapter(url, times=3):  # times 控制异常重试的次数, 超过这个次数任然会报错
    try:
        response = requests.get(url=url, headers=headers, timeout=0.1)
        html_data = response.text
        # print(html_data)
        selector = parsel.Selector(html_data)

        title = selector.css('h1.wap_none::text').re(' (.*)')[0]  # 标题
        contend = selector.css('#chaptercontent::text').getall()  # 小说数据
        contend = [i.replace('\u3000\u3000', '') for i in contend]
        contend = '\n'.join(contend)

        file_path = '小说\\' + str(count) + title + '.txt'
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(contend)
            print('保存完成:', file_path)
    except Exception as e:
        print(e)
        if times >= 1:  # 可以控制异常重试的次数
            get_one_chapter(url, times=times - 1)  # 利用函数的递归的特性, 异常重试, 一直重试, 知道成功为止
            print('*' * 100)


if __name__ == '__main__':
    count = 1  # 全局变量, 用于小说章节的名字

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = 'https://www.bqg70.com/book/1031/'
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    dds = selector.css('.listmain>dl dd')
    for dd in dds:
        title = dd.css('a::text').get()
        link_url = dd.css('a::attr(href)').get()
        all_url = 'https://www.bqg70.com' + link_url
        # print(all_url)

        if '展开全部章节' in title:
            continue

        get_one_chapter(all_url)

        count += 1
