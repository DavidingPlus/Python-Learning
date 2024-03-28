my_list = {"黑马程序员", "传智播客", "黑马程序员", "传智播客",
           "itheima", "itcast", "itcast", "best"}

newlist = set()

for element in my_list:
    print(f"my_list的元素是: {element}")
    newlist.add(element)
print(f"新集合的结果是: {newlist}")
