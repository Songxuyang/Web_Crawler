
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

tel = "18123115458"

import re

result = re.sub(tel[3:7], '****', tel, flags=re.S)
print(result)