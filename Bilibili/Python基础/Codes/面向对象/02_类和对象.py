# 设计一个闹钟类
class Clock:
    id = None  # 序列号
    price = None  # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


# 构造2个闹钟对象让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID: {clock1.id},价格: {clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID: {clock2.id},价格: {clock2.price}")
clock2.ring()
