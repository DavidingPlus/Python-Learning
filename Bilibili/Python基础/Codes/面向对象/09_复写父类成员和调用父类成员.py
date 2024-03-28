from typing import Union


class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")


class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式,确保通话的时候省电")
        # 调用父类成员
        # 父类名.成员方法(self) 父类名.成员变量
        # super().成员方法() super.成员变量

        # 方法1
        # print(f"父类的厂商是: {Phone.producer}")
        # Phone.call_by_5g(self)  # 这个self必须有!!!

        # 方法2
        print(f"父类的厂商是: {super().producer}")
        super().call_by_5g()  # 这个self可以不要!!!

        print("关闭CPU单核模式,确保性能")


phone = MyPhone()
print(phone.producer)
phone.call_by_5g()

# 类型注解 提醒自己这是什么类型
var_1: int = 12345


def add(x: int, y: int) -> int:
    return x+y


# Union类型注解
# from typing import Union
my_list: list[Union[str, int]] = [1, 2, "ITHEIMA", "ITCAST"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
