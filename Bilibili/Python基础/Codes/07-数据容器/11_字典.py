my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()

print(f"字典1的内容是: {my_dict1},类型是: {type(my_dict1)}")
print(f"字典2的内容是: {my_dict2},类型是: {type(my_dict2)}")
print(f"字典3的内容是: {my_dict3},类型是: {type(my_dict3)}")

# python中的key不可以重复!!!
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}  # 这个88把前面的99给覆盖掉了,不允许重复key
print(f"重复key的字典1的内容是: {my_dict1}")

# 从字典中获取数据
print(my_dict1["王力宏"])
print(my_dict1["周杰伦"])
print(my_dict1["林俊杰"])

# 字典的key和value可以是任何数据类型(key不可以类型)
my_dict4 = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    },
    "周杰伦": {
        "语文": 88,
        "数学": 66,
        "英语": 55
    },
    "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是: {my_dict4}")

score = my_dict4["周杰伦"]["语文"]
print(f"周杰伦的语文分数是: {score}")

# 字典[key]=value 如果key不存在则新增元素,存在则更新数据
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
my_dict1["张信哲"] = 66
print(f"字典经过新增后,结果: {my_dict1}")
my_dict1["周杰伦"] = 33
print(f"字典经过更新后,结果: {my_dict1}")

# 删除元素 字典.pop(key)
score = my_dict1.pop("周杰伦")
print(f"字典被移除了一个元素,结果是: {my_dict1},周杰伦的考试分数是: {score}")

# 清空元素 clear

# 获取全部的key
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
keys = my_dict1.keys()
print(f"字典的全部keys是: {keys}")

# 遍历字典
for key in keys:
    print(f"字典的key是: {key}")
    print(f"字典的value是: {my_dict1[key]}")

for key in my_dict1:  # 对字典遍历得到key!!!
    print(f"2字典的key是: {key}")
    print(f"2字典的value是: {my_dict1[key]}")
