# 元字符匹配
import re
s = "itheima1 @@python2 !!666 ##itcast3"

# 单字符匹配
result = re.findall(r"\d", s)  # r表示字符串当中的转义字符无效,就是个普通字符
print(result)

result = re.findall(r"\W", s)  # 找到特殊字符
print(result)

result = re.findall(r"[a-zA-Z]", s)  # 找到英文字符
print(result)
