# 导入自定义模块
# import my_module1
# print(my_module1.my_add(10, 20))

# 调用多个模块的时候,如果模块当中有同名功能,后面的模块会把前面的覆盖掉,用的是后面导入的功能!!!
# from my_module1 import test
# from my_module2 import test
# print(test(100, 50))

# __main__ 变量
# from my_module1 import test

# __all__ 变量 是个列表!!
# 如果一个模块文件中有"__all__"变量,当使用 from xxx import * 导入时,只能导入这个列表中的元素!!!
from my_module1 import *
print(test_a(1, 2))
print(test_b(2, 1))
