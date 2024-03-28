def list_while_func():
    my_list = ["传智教育", "黑马程序员", "Python"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素: {element}")
        index += 1


list_while_func()


def list_for_func():
    my_list = ["传智教育", "黑马程序员", "Python"]
    # for 临时变量 in 数据容器 : (将数据容器中的内容一一给临时变量)
    # for index in range(len(my_list)):
    #     element = my_list[index]
    for element in my_list:
        print(f"列表的元素: {element}")


list_for_func()
