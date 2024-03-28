# 设置一个类 内置私有成员变量和成员方法
class Phone:
    # 以两个下划线开头 为 私有成员!!!!
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足,无法使用5g通话,并已设置为单核运行进行省电")


phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5g()
