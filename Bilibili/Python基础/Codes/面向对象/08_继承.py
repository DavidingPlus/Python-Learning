class Phone:
    IMEI = None  # 序列号
    producer = "Itcast"  # 厂商

    def call_by_4g(self):
        print("4g通话")


# 单继承
class Phone2022(Phone):
    face_id = "10001"  # 面别识别id

    def call_by_5g(self):
        print("2022年新功能: 5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 用pass表示这里是空的,让这里不产生错误


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 两个父类都有同名成员,谁先传入谁的优先级高,调用谁!!!这里就是Phone
print(phone.producer)
