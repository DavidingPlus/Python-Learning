# get请求
# 获取豆瓣电影的第一页的数据并且保存起来
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}

# 1.请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 2.获取相应的数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
# print(content)

# 3.数据下载到本地
# open方法默认情况下gbk编码
with open("/mnt/d/Code/Python/Bilibili/爬虫/10_douban.json",
          "w", encoding="UTF-8")as file:
    file.write(content)
