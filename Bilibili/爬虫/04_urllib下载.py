import urllib.request

# 下载网页
url_page = "http://www.baidu.com"

# url代表的是下载的路径
urllib.request.urlretrieve(url_page, "04_baidu.html")

# 下载图片
url_img = "https://img2.baidu.com/it/u=2310341791,3457471102&fm=253&fmt=auto&app=120&f=JPEG?w=640&h=427"
urllib.request.urlretrieve(url=url_img, filename="04_James.jpg")

# 下载视频
# url_video = ""
# urllib.request.urlretrieve(url_video, "1.mp4")
