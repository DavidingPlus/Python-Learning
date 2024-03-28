def user_info(name, age, gender):
    print(f"姓名是: {name},年龄是: {age},性别是: {gender}")


# 位置参数
user_info("小明", 20, "男")

# 关键字传参
# 可以不按照固定数据 按照键值对方式传入
# 可以和位置参数混用,位置参数必须在前,且匹配参数顺序,但是关键字参数之间不存在先后顺序
user_info(name="小王", age=11, gender="女")
user_info(age=10, gender="女", name="潇潇")  # 可以不按照参数的定义顺序传参
user_info("甜甜", gender="女", age=9)


def user_info2(name, age, gender="男"):  # 设置默认值必须在最后面!!!!!
    print(f"姓名是: {name},年龄是: {age},性别是: {gender}")


# 缺省参数 传递参数的时候有默认值
user_info2("小天", 13)
user_info2("小天", 13, "女")

# 不定长参数


def user_info3(*args):  # 位置参数
    print(f"args参数的类型是: {type(args)},内容是: {args}")
# args进来后会将接收的数据默认合并为一个元组类型!!!!!


user_info3("Tom")
user_info3("Tom", 18)


def user_info4(**kwargs):  # 关键字传递
    print(f"kwargs参数的类型是: {type(kwargs)},内容是: {kwargs}")


# 参数是"键=值"的形式传递 传入的数据作为字典存在
user_info4(name="Tom", age=18, id=110)
