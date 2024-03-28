# 使用的场景: 数据采集的时候 需要绕过登录 然后进入到某个界面
# 并没有进入到个人信息页面 而是跳转到了登陆页面!!!!

# 什么情况访问不成功
# 请求头的信息不够 所以访问不成功!!!


import urllib.request

url = "https://m.weibo.cn/profile/2803301701"

headers = {
    # ':authority': ' m.weibo.cn',
    # ':method': ' GET',
    # ':path': ' /profile/info?uid=2803301701',
    # ':scheme': ' https',
    'accept': ' application/json, text/plain, */*',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # cookie中携带者你的登录信息 如果有登录之后的cookie 那么就可以携带者cookie进入到任何页面!!!
    'cookie': ' WEIBOCN_FROM=1110006030; SUB=_2A25Ou9q0DeRhGeFK61IQ9ybNyj-IHXVqR-b8rDV6PUJbkdAKLRP3kW1NQ712IGh_owRYvDfDXl-3WsjW45IPt9HK; _T_WM=63824081534; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174; XSRF-TOKEN=a361f1',
    # referer 判断当前路径是不是由上一个路径进来的 一般做 图片的防盗链!!!
    'referer': 'https://m.weibo.cn',
    'sec-ch-ua': ' "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode("utf-8")

# 将数据保存到本地
with open("/mnt/d/Code/Python/Bilibili/爬虫/14_weibo.html",
          "w", encoding="utf-8")as file:
    file.write(content)
