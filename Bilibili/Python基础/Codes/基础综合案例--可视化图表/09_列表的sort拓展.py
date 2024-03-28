# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]


# 排序,基于待命函数
def choose_sort_key(element):
    return element[1]  # 意思是让列表基于数字进行排序 默认是升序


# my_list.sort(key=choose_sort_key, reverse=False)
# print(my_list)

my_list.sort(key=lambda element: element[1], reverse=False)
print(my_list)
