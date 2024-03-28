# 正则表达式,定义好规则验证目标是否符合规则
import re

# match 从头匹配 从0号元素开始往后找!!!!
# 如果头部不匹配,也不理会后面的是否匹配!!!!
s = "1python itheima python python"
result = re.match("python", s)
print(result)
# print(result.span())  # (0,6)
# print(result.group())  # "python"

# search 搜索整个字符串找出匹配的,找到第一个的就停止,不会继续向后
result = re.search("python", s)
print(result)

# findall 找出全部匹配项!!!
result = re.findall("python", s)
print(result)
