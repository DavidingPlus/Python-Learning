# 集合 不支持元素的重复 自带去重功能 内部无序
# 集合定义 {}
# 空集合
# 变量名称 = {}
# 变量名称 = set()

my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员",
          "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()
print(f"my_set的内容是: {my_set},类型是: {type(my_set)}")
print(f"my_set_empty的内容是: {my_set_empty},类型是: {type(my_set_empty)}")

# 集合无序,所以集合不支持下标索引访问
# 集合和列表一样,允许修改

# 添加新元素 add
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后,结果是: {my_set}")

# 移除元素 remove
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后,结果是: {my_set}")

# 随机取出一个元素
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()
print(f"my_set随机取出一个元素是: {element},取出后结果是: {my_set}")

# 取出两个集合的差集 集合1有而2没有
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1和set2的差集为: {set3}")
print(f"取差集后,原有set1的内容是: {set1}")
print(f"取差集后,原有set2的内容是: {set2}")

# 消除两个集合的交集 集合1消除和集合2相同的元素 集合1变化 2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除后,set1的内容是: {set1}")
print(f"消除后,set2的内容是: {set2}")

# 两个集合合并 得到新集合 需要去除交集 因为不重复 原先两集合不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"合并后,set3内容是: {set3}")
print(f"合并后,set1内容是: {set1}")
print(f"合并后,set2内容是: {set2}")

# 集合的遍历
# 集合不支持下标索引!!!
set1 = {6, 1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有: {element}")

while set1 != set():
    element = set1.pop()  # 但是这样原来的集合就被破坏了
    print(f"集合的元素有: {element}")
