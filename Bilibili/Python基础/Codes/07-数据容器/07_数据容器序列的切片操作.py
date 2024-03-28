# 序列: 内容连续,有序,可使用下标索引的一类数据容器
# 列表 元组 字符串 均可以视为序列
# 切片:从大序列中取出一个小序列 序列[起始下标:结束下标:步长] 从起始开始到结束 不包含结束

my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(f"结果1: {result1}")

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # 起始和结束不写表示从头到尾,步长为1可以省略
print(f"结果2: {result2}")

my_str = "01234567"
result3 = my_str[::2]
print(f"结果3: {result3}")

my_str = "01234567"
result4 = my_str[::-1]  # 等同于将序列反转
print(f"结果4: {result4}")

my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_tuple[3:1:-1]
print(f"结果5: {result5}")

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果6: {result6}")
