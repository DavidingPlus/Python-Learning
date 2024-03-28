str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数变量
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是: {count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是: {count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度是: {count}")

# 函数


def my_Len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是: {count}")


my_Len(str1)
my_Len(str2)
my_Len(str3)
