# open()打开函数
# open(name,mode,encoding)
# name:文件名路径
# mode:打开模式 只读r 写入w 追加a
# encoding:编码格式

# 打开文件
file = open(
    "/mnt/d/Code/Python/Bilibili/文件操作/python.txt", "r", encoding="UTF-8"
)  # encoding的位置不在第三位,需要使用关键字传参 第三位是个buffering=-1的形参,省略了
print(type(file))

# 读取文件 read(num)
# num 从文件中读取的数据长度(字节) 没有传入就全读取
# print(f"读取3个字节的结果: {file.read(3)}")
# print(f"read方法读取全部内容的结果:\n{file.read()}")

# # !!!如果连续调用read或者readlines,后续的read会从上次的read结尾接着开始读取!!!!!

# # readlines() 按照行的方式一次性读取文件,并且返回一个列表,一行的数据是一个元素
# lines = file.readlines()
# print(f"line对象的类型是: {type(lines)}")
# print(f"line对象的内容是: {lines}")

# readline() 一行一行读取 会记录上次位置
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# print(f"第一行数据是: {line1}")
# print(f"第二行数据是: {line2}")
# print(f"第三行数据是: {line3}")

# for循环读取文件行
# for line in file:
#     print(f"每一行数据是: {line}")

# 文件的关闭
# file.close()

# with open 语法 可以在调用文件的时候自动帮我们实现文件的关闭操作
with open("/mnt/d/Code/Python/Bilibili/文件操作/python.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(f"每一行的数据是； {line}")
