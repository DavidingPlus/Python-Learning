class Animal:
    def speak(self):
        pass  # 空实现 和C++一样 抽象类


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noice(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noice(dog)
make_noice(cat)
