mystr = "itheima itcast boxuegu"

# 统计it字符
count = mystr.count("it")
print(f"字符串{mystr}中有: {count}个it字符")

# 将空格替换为"|"
new_mystr = mystr.replace(" ", "|")
print(f"字符串{mystr},被替换空格后,结果: {new_mystr}")

# 分割
new_mystr_list = new_mystr.split("|")
print(f"字符串{new_mystr},按照|分割后,得到: {new_mystr_list}")
