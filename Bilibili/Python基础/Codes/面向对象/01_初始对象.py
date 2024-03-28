class Student:
    name = None  # 记录学生姓名
    gender = None  # 记录学生性别
    nationality = None  # 国籍
    native_place = None  # 籍贯
    age = None  # 年龄

    def say_hi(self):  # self必须存在于传参列表中,但是在调用时不需要,相当于是c++中的*this
        print(f"大家好啊,我是{self.name},请大家多多关照")

    def say_hi2(self, msg):  # self必须存在于传参列表中,但是在调用时不需要,相当于是c++中的*this
        print(f"大家好啊,我是{self.name},{msg}")


stu_1 = Student()
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31

print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
stu_1.say_hi()
stu_1.say_hi2("小伙子我看好你")
