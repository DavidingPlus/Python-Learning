# 需求 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码
import urllib.request
import urllib.parse
# quote方法:将汉字转换为unicode编码

url = "https://www.baidu.com/s?wd="

# 请求对象定制为了反爬的第一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}

# 将周杰伦三个字变成unicode编码的格式
# 我们需要以来urllib.parse
name = urllib.parse.quote("周杰伦")
url = url+name

request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取相应的内容
content = response.read().decode("utf-8")
print(content)
