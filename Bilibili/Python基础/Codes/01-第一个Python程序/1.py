# print函数

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('helloworld')

# 含有运算符的表达式
print(3+1)

# 将数据输出到文件中  注意点:1.所指定的盘符要存在 2.使用file =fp
fp = open('D:/Code/Python/Bilibili/11.24/text.txt', 'a+')
print('helloworld', file=fp)  # 如果文件不存在就创建,存在就在文件内容后面继续追加
fp.close()


# 不进行换行输出(输出内容是在一行)
print('hello', 'world', 'Python')
