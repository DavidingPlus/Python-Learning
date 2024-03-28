# 工厂模式
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Person_Factory:
    def get_person(self, p_Type):
        if p_Type == "w":
            return Worker()
        elif p_Type == "s":
            return Student()
        elif p_Type == "t":
            return Teacher()


pf = Person_Factory()
worker = pf.get_person("w")
studetn = pf.get_person("s")
teacher = pf.get_person("t")
