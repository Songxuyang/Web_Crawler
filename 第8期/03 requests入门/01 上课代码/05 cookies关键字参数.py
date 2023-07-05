import requests


url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

data = {
    'from': 'zh',
    'to': 'en',
    'query': '早上好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '282438.44151',
    'token': '6ab90f62e10e7c3012f12686fd8f7900',
    'domain': 'common'
}

headers = {
    # 可以直接写到请求头中
    # 'Cookie': 'BAIDUID=B3CB6D866941A6F011C3E888522F435D:FG=1; __yjs_duid=1_b28b31ba4419ca95e2235341c1ab03001642426424402; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; APPGUIDE_10_0_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSTM=1642427594; BIDUPSID=FC54E7FEB1C34E2391F37964BA55C63F; H_PS_PSSID=35417_35105_35630_35457_34584_35491_35701_35688_35316_26350_22159; delPer=0; PSINO=6; BA_HECTOR=010k8181a12004akpf1gug5i60r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1642426424,1642600007; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1642600007; ab_sr=1.0.1_YmVmZDAwYmE0YjU2ZDY2MzcyZDM0ZjQ2MDg2ZjVjMTM1ZTM1YWM5MzljNzljZmRhOWMwZjgzNWJmZjhiMTEwNGFmOWUwMzZmYmMxZGJlMmFkYzdiNzQyNzg5YWFmM2E4',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

# 用字典构建每个cookies的片段
cookies = {
'BAIDUID=B3CB6D866941A6F011C3E888522F435D:FG': '1',
# '__yjs_duid':'1_b28b31ba4419ca95e2235341c1ab03001642426424402',
# 'FANYI_WORD_SWITCH':'1',
# 'HISTORY_SWITCH':'1',
# 'REALTIME_TRANS_SWITCH':'1',
# 'SOUND_PREFER_SWITCH':'1',
# 'SOUND_SPD_SWITCH':'1',
# 'APPGUIDE_10_0_2':'1',
# 'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
# 'PSTM':'1642427594',
# 'BIDUPSID':'FC54E7FEB1C34E2391F37964BA55C63F',
# 'H_PS_PSSID':'35417_35105_35630_35457_34584_35491_35701_35688_35316_26350_22159',
# 'delPer':'0',
# 'PSINO':'6',
# 'BA_HECTOR':'010k8181a12004akpf1gug5i60r',
# 'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574':'1642426424,1642600007',
# 'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574':'1642600007',
# 'ab_sr':'1.0.1_YmVmZDAwYmE0YjU2ZDY2MzcyZDM0ZjQ2MDg2ZjVjMTM1ZTM1YWM5MzljNzljZmRhOWMwZjgzNWJmZjhiMTEwNGFmOWUwMzZmYmMxZGJlMmFkYzdiNzQyNzg5YWFmM2E4'

}

# cookies 是请求提交cookies的关键字
response = requests.post(url=url, data=data, headers=headers, cookies=cookies)
json_data = response.json()
print(json_data)


