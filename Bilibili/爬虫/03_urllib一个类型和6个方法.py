import urllib.request

url = "http://www.baidu.com"
# 模拟浏览器向服务器发送请求
response =   urllib.request.urlopen(url)

# 一个类型和六个方法
# print(type(response))  # HTTPResponse

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)

# content = response.read(5)  # 读5个字节!!!
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 读取所有行
# content = response.readlines()
# print(content)

# 返回状态码 如果是200 证明我们的逻辑没有错
# print(response.getcode())

# 返回的是url地址
print(response.geturl())

# 获取的是一个状态信息
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders
