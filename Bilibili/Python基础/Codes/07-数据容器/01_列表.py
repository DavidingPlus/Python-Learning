# 列表字面量
# [elem1, elem2, elem3, ……]

# 定义空列表
# 变量名称 = []
# 变量名称 = list()
my_list = ["itheima", 666, True]
print(my_list)
print(type(my_list))

my_list = ["Tom", "Lily", "Rose"]
# 从前向后从0开始 每次+1
# 从后向前从-1开始 每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])

# 查找某元素的下标 index(元素)
my_list = ["itcast", "itheima", "python"]
index = my_list.index("itheima")
print(f"itheima在列表中的下表索引值是: {index}")
# 如果不存在 会报错
# index = my_list.index("hello")

# 插入元素 insert(下标,元素)
my_list = ["itcast", "itheima", "python"]
my_list.insert(1, "best")
print(f"列表插入元素后,结果是: {my_list}")

# 追加元素 append(元素) 将元素追加到列表尾部
my_list.append("黑马程序员")
print(f"列表追加元素后,结果是: {my_list}")

# 追加元素2 extend(其他数据容器) 将这个数据容器全部追加到这个容器后面
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"列表追加一个新的列表后,结果是: {my_list}")

# 删除元素 del 列表[下标]
my_list = ["itcast", "itheima", "python"]
del my_list[2]
print(f"列表删除元素后,结果是: {my_list}")

# 方法2 列表.pop(下标)
my_list = ["itcast", "itheima", "python"]
element = my_list.pop(2)
print(f"通过pop方法取出元素后,结果是: {my_list},取出的元素是: {element}")

# 删除某元素在列表中的第一个匹配项 列表.remove(元素)
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
my_list.remove("itheima")
print(f"通过remove移除元素后,结果是: {my_list}")

# 清空列表 列表.clear()
my_list.clear()
print(f"列表被清空了,结果是: {my_list}")

# 统计某个元素在列表内数量 列表.count(元素)
my_list = ["itcast", "itheima", "itcast", "itheima", "python"]
count = my_list.count("itheima")
print(f"列表中itheima的数量是: {count}")

# 统计列表中元素数量 len(列表)
count = len(my_list)
print(f"列表的元素数量总共有: {count}")
