# 内存地址没有多大作用,我们可以通过 __str__ 方法,控制类转换为字符串的行为!!!
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 魔术方法
    def __str__(self) -> str:
        return f"Student类对象,name: {self.name},age: {self.age}"

    # __lt__ 魔术方法 小于符号比较方法
    def __lt__(self, other) -> bool:
        return self.age < other.age

    # __le__ 魔术方法 小于等于比较方法
    def __le__(self, other) -> bool:
        return self.age <= other.age

    # __eq__ 魔术方法 比较运算符方法
    def __eq__(self, other) -> bool:
        return self.age == other.age


stu1 = Student("周杰伦", 31)
stu2 = Student("林俊杰", 36)
print(stu1)
# print(str(stu1))
print(stu1 < stu2)
print(stu1 >= stu2)
