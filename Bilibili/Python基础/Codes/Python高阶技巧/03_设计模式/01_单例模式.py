# 单例模式的主要目的是确保某一个类当中只有一个实例存在!!!并提供一个全局访问点
from str_tools import str_tool

s1 = str_tool
s2 = str_tool

# 这两个id一模一样!!!
print(id(s1))
print(id(s2))
