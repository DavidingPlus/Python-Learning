# json格式要求
# 字典
# {"name": "admin", "age": 18}

# 列表 元素是字典
# [{"name": "admin", "age": 18},
#  {"name": "root", "age": 19},
#  {"name": "张三", "age": 20}]

# python数据和json数据的相互转换
# 导入json模块
import json

# 准备列表,列表内每个元素都是字典,将其转换为json dumps()
data = [{"name": "admin", "age": 18},
        {"name": "root", "age": 19},
        {"name": "张三", "age": 20}]
json_str = json.dumps(data, ensure_ascii=False)  # 里面包含中文包含这个参数来正确输出中文
print(type(json_str))
print(json_str)

# 准备字典,将字典转换为json dumps()
d = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转换为python数据
str = '[{"name": "admin", "age": 18},{"name": "root", "age": 19},{"name": "张三", "age": 20}]'
l = json.loads(str)
print(type(l))
print(l)

str = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(str)
print(type(l))
print(l)
