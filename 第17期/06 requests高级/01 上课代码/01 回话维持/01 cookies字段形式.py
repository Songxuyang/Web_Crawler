import requests


url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    # 在请求头中传递cookies
    'Acs-Token': '1687354513445_1687354530324_U0QUCd0KA/F7BYp74tXcgnoFsNtOOxo4iufv+Hk5xXqn2+frnr0XUBVQuvTA3dfcUNYPfwpE/Y/JKtFNRsVrPchR4jO1sLxlmyw0hvh3usx51exIBKNRgH4NQXBDqAt3YJadXkNDjTR67nCTZiw+RJk7dF5HUYF5tJQ2b6P7MOd74rkMTn+xiwSraonXITV1rfLX6Pljrf7BCAACg8KuPEJplI1HlqnRHpoq54OKlcGiWXm2ZWfAcq4EVmqb1nVSge61u6U85j/n7R3JJ4LA96Vw0kcKtFi5X8GAw2SHCZ1fAZREBFeYdhG6fXVEZP+e6mkHJn/yUmb3IUb+GxtEhS1alaQMFv9QQZSBx6tXbfW6ncLHgcZfcDTqoKWSe3tdX39s1qnOEoWGvwLFFe/XMszJzUdMuOhndbQPdjkofy58aIlMTJErOTeELJ+21UOigR2VuwxiD/k9oI7vmMH0UUYzjVqojZcGNU2GrWMcfto=',
    # 'Cookie': "BIDUPSID=A8D9EA340531252B16551CBD43A8D395; PSTM=1681976911; BAIDUID=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=131862_114552_216844_213346_214803_219942_110085_243887_244712_249892_256348_256447_256739_254317_257586_257996_258372_258375_230288_259102_259287_258772_234207_234295_253022_260335_260806_259299_253631_261575_261718_261459_261983_259782_260440_261793_259629_236312_262490_262452_261869_262607_262677_262597_262604_249411_259519_259948_262743_262746_262913_263190_256998_263221_263306_263279_243615_263343_261683_263434_254299_261411_263584_257289_262439_262533_263644_262408_262910_257169_262289_263906_263363_256419_264175_264089_264228_257442_256225_262260_255224_264018_264368_259558_256083_264383_264423_264452_264285_256152_264626_264246_258698_264749_261934_264820_264136_261035_261663; H_PS_PSSID=38516_36550_38686_38860_38793_38841_38581_38802_38828_38840_38640_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; delPer=0; PSINO=6; BA_HECTOR=ah2g2ka48k0g8h2h00a4842h1i95r4t1p; ZFY=CMMricp5SfogOfi1RswFaP4NBZN6t5zy:Axurblw8al4:C; BCLID=8504214758825411246; BCLID_BFESS=8504214758825411246; BDSFRCVID=TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1687354513; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1687354513; ab_sr=1.0.1_NDJjZTI3ZGQwZjJhN2I2YThjMWMxNDgxNWJhOGM5YTEwMjYwYWM0NDU3Mjk0Y2MxZTAyNWE0MzIyNDlhYjJmYjQ5NDUxNzEzOTI4YmIyZjUyNDFiNjFkM2Q0ZTYyMjZjMGU1ZTU3MDFiMTNhMWU5NTY2NDdlYWExZWEyZDZiMWNkNGVjMTExNTQyM2MyNzYxYThiNzAzYmUxNTAxZGI2NA==",
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '232427.485594',
    'token': '351b986af9e8a703056ff2f022cdf830',
    'domain': 'common',
    'ts': '1687354530307',
}

# 构建cookies字典
# cookies = {'Cookie': 'BIDUPSID=A8D9EA340531252B16551CBD43A8D395; PSTM=1681976911; BAIDUID=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=131862_114552_216844_213346_214803_219942_110085_243887_244712_249892_256348_256447_256739_254317_257586_257996_258372_258375_230288_259102_259287_258772_234207_234295_253022_260335_260806_259299_253631_261575_261718_261459_261983_259782_260440_261793_259629_236312_262490_262452_261869_262607_262677_262597_262604_249411_259519_259948_262743_262746_262913_263190_256998_263221_263306_263279_243615_263343_261683_263434_254299_261411_263584_257289_262439_262533_263644_262408_262910_257169_262289_263906_263363_256419_264175_264089_264228_257442_256225_262260_255224_264018_264368_259558_256083_264383_264423_264452_264285_256152_264626_264246_258698_264749_261934_264820_264136_261035_261663; H_PS_PSSID=38516_36550_38686_38860_38793_38841_38581_38802_38828_38840_38640_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; delPer=0; PSINO=6; BA_HECTOR=ah2g2ka48k0g8h2h00a4842h1i95r4t1p; ZFY=CMMricp5SfogOfi1RswFaP4NBZN6t5zy:Axurblw8al4:C; BCLID=8504214758825411246; BCLID_BFESS=8504214758825411246; BDSFRCVID=TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1687354513; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1687354513; ab_sr=1.0.1_NDJjZTI3ZGQwZjJhN2I2YThjMWMxNDgxNWJhOGM5YTEwMjYwYWM0NDU3Mjk0Y2MxZTAyNWE0MzIyNDlhYjJmYjQ5NDUxNzEzOTI4YmIyZjUyNDFiNjFkM2Q0ZTYyMjZjMGU1ZTU3MDFiMTNhMWU5NTY2NDdlYWExZWEyZDZiMWNkNGVjMTExNTQyM2MyNzYxYThiNzAzYmUxNTAxZGI2NA=='}


# 3将每个cookies片段构建键值对
cookies = {
'BAIDUID':'A8D9EA340531252BDEF2C13A73AFA5E7:FG=1',
'BAIDUID_BFESS':'A8D9EA340531252BDEF2C13A73AFA5E7:FG=1',
'ZFY':'CMMricp5SfogOfi1RswFaP4NBZN6t5zy:Axurblw8al4:C',
'BIDUPSID': 'A8D9EA340531252B16551CBD43A8D395',
'PSTM': '1681976911',
'APPGUIDE_10_0_2': '1',
'REALTIME_TRANS_SWITCH': '1',
'FANYI_WORD_SWITCH': '1',
'HISTORY_SWITCH': '1',
'SOUND_SPD_SWITCH': '1',
'SOUND_PREFER_SWITCH': '1',
'H_WISE_SIDS': '131862_114552_216844_213346_214803_219942_110085_243887_244712_249892_256348_256447_256739_254317_257586_257996_258372_258375_230288_259102_259287_258772_234207_234295_253022_260335_260806_259299_253631_261575_261718_261459_261983_259782_260440_261793_259629_236312_262490_262452_261869_262607_262677_262597_262604_249411_259519_259948_262743_262746_262913_263190_256998_263221_263306_263279_243615_263343_261683_263434_254299_261411_263584_257289_262439_262533_263644_262408_262910_257169_262289_263906_263363_256419_264175_264089_264228_257442_256225_262260_255224_264018_264368_259558_256083_264383_264423_264452_264285_256152_264626_264246_258698_264749_261934_264820_264136_261035_261663',
'H_PS_PSSID': '38516_36550_38686_38860_38793_38841_38581_38802_38828_38840_38640_26350',
'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
'delPer': '0',
'PSINO': '6',
'BA_HECTOR': 'ah2g2ka48k0g8h2h00a4842h1i95r4t1p',
'BCLID': '8504214758825411246',
'BCLID_BFESS': '8504214758825411246',
'BDSFRCVID': 'TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
'BDSFRCVID_BFESS': 'TO8OJexroG0ZmSbfuwStIGta5LweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
'H_BDCLCKID_SF': 'tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j',
'H_BDCLCKID_SF_BFESS': 'tRAOoC_-tDvDqTrP-trf5DCShUFsLU4OB2Q-XPoO3KJADfOPbRob0n0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjDMDTJy3j',
'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1687354513',
'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1687354513',
'ab_sr': '1.0.1_NDJjZTI3ZGQwZjJhN2I2YThjMWMxNDgxNWJhOGM5YTEwMjYwYWM0NDU3Mjk0Y2MxZTAyNWE0MzIyNDlhYjJmYjQ5NDUxNzEzOTI4YmIyZjUyNDFiNjFkM2Q0ZTYyMjZjMGU1ZTU3MDFiMTNhMWU5NTY2NDdlYWExZWEyZDZiMWNkNGVjMTExNTQyM2MyNzYxYThiNzAzYmUxNTAxZGI2NA==',

}
# cookies关键字
response = requests.post(url=url, data=data, headers=headers, cookies=cookies)
json_data = response.json()
print(json_data)

# 请求会校验用户cookies字段
"""
cookies怎么来的?
    服务器生成: 请求与响应间生成cookies的片段信息  Set-cookie
    浏览器生成: 一般在我们模拟请求的时候服务器不会校验
    js生成: JavaScript, 逆向分析
    
代码怎么维持用户的cookies状态?
"""
