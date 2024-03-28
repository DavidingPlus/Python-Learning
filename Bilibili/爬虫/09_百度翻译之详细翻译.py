import json
import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

# 请求对象定制
# Cookie 起绝对性因素
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding':' gzip, deflate, br',
    # 'Accept-Language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Acs-Token': ' 1673165146375_1673248783415_a+vchFDHZjRVA6BeqPnLQXaBoXiWZoxBubRmP6QQiM8C44kQNpn894Jy6H8GxCMIle73YsHuH21KqG9qI5j1OpR/VvULD8rcGnHUhBMrViYloausVnVoo4f0qklKqfsYCxPpzmAaPiMpvg+AUAxSddrgscVNmxlsex1yGzvqdkCUfGeO7kTSZR9GXiZBjTr9Yltqg/7to7eD47sevqSu9Jvxki1TZvyI5nLH2E8pxAUtHrw9uYGIdO9F9gANHcVgfBT5bk367iNJx/vzrTB7KS1wAGqgfJq9HhZqb1nozJgKEVj7EMa2Op9g6sjp/oWgN0VP7o04V9OLqJWnE5tedQ==',
    # 'Connection': ' keep-alive',
    # 'Content-Length': ' 116',
    # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'newlogin=1; BAIDUID=2CC1E95939B61298B2D7B23BB80CF6E8:FG=1; BIDUPSID=2CC1E95939B61298B2D7B23BB80CF6E8; PSTM=1671719096; __yjs_duid=1_a7c79e6a080a9195877a20833b9326021672759587511; BAIDUID_BFESS=2CC1E95939B61298B2D7B23BB80CF6E8:FG=1; ZFY=:BDFzR1MgiSt40vqpa0zSWGdpufAkSllD7weWDSXhs1g: C; H_PS_PSSID=36552_37647_37910_38015_37625_36920_38035_37990_37934_37874_26350_22159_37881; BA_HECTOR=a1a18k8h84al04a02l8h0huc1hrn0d61k; PSINO=6; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673232824; ab_sr=1.0.1_NjYxZjg4Mzc4MjZkZDRjNzI1YTdjYzY1NmQ5MDc0Y2RkNzZkMzlmYjQzODcxYzFhY2RkM2FiNTE5N2ZiNjU1YjQxNDE0NzUyMWRiZDIxYTcyYWI0NzhkZWE2YTU0Y2EzNTcwNDIzZDc4MjNlYzI5MjE0NzQ2ODZlNjliMzRmYzczYjMzNGVhZTI5YjZiMWRiZjIyMDI2ZmI3MjNhMTQ2MA==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1673248783',
    # 'Host': ' fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'sec-ch-ua': ' "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    # 'sec-ch-ua-mobile': ' ?0',
    # 'sec-ch-ua-platform': ' "Windows"',
    # 'Sec-Fetch-Dest': ' empty',
    # 'Sec-Fetch-Mode': ' cors',
    # 'Sec-Fetch-Site': ' same-origin',
    # 'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    # 'X-Requested-With': ' XMLHttpRequest',
}

data = {
    "from": "en",
    "to": "zh",
    "query": "Love",
    "simple_means_flag": "3",
    "sign": "530557.850764",
    "token": "a1a2303189bc29dcbb7ea6726bd12138",
    "domain": "common"
}
# post请求的参数必须进行编码并且要调用encode方法
data = urllib.parse.urlencode(data).encode("utf-8")

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取相应的数据
content = response.read().decode("utf-8")
# print(content)

# 转换为json
obj = json.loads(content)
print(obj)
