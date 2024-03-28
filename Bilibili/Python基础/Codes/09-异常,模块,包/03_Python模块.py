# 导入的语法
# [from 模块名] import [模块, 类, 变量, 函数, * ][as 别名]

#例: 导入time模块
# import time
# print("你好")
# time.sleep(3)  # 这个sleep的单位是秒!
# print("我不好")

# 使用from导入time的sleep功能(函数)
# from time import sleep
# print("你好")
# sleep(3)
# print("我不好")

#使用* 导入time模块的全部功能
# from time import *  # * 表示全部功能的意思
# print("你好")
# sleep(3)
# print("我不好")

# 使用as给指定功能加上别名
import time as fuck
print("你好")
fuck.sleep(3)
print("我不好")
