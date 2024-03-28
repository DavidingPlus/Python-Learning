my_str = "itheima and itcast"
# 字符串和元组一样,是一个无法修改的数据容器
# 如果硬要修改,相当于创造一个新的字符串

# 查找特定字符串的下标 index()
val = my_str.index("and")
print(f"在字符串{my_str}中,查找and,起始下标为: {val}")

# 字符串替换 replace(字符串1,字符串2)
# 注意不是修改字符串本身,而是得到了一个新字符串
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str},进行替换后得到: {new_my_str}")

# 字符串的分割 split(分割字符串)
# 按照指定的分隔符 分割字符串 得到多个字符串 存入列表中
# 字符串本身不变 得到了一个新的列表对象
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str},进行split分割后得到: {my_str_list},类型是{type(my_str_list)}")

# 字符串规整操作 去除前后指定字符串 strip
# 不传参数 去除头和尾的空格
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip后,得到: {new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后,得到: {new_my_str}")
