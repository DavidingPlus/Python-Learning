# urlencode应用情景:多个参数的时候 用&拼接
# https://www.baidu.com/s?wd=周杰伦&sex=男

import urllib.parse
import urllib.request

base_url = "https://www.baidu.com/s?"

data = {
    "wd": "周杰伦",
    "sex": "男",
    "location": "中国台湾省"
}
data = urllib.parse.urlencode(data)
url = base_url+data

# 请求对象定制为了反爬的第一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}


request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取相应的内容
content = response.read().decode("utf-8")
print(content)
