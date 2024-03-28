money = 5000000
name = None


def check_money(name):  # 查询余额函数
    print(f"{name},您好,您的余额剩余: {money}元")
    print('\n')


def save_money(name):  # 存款函数
    num = int(input("存款: "))
    global money  # money在函数内部定义为全局变量!!!
    money += num
    print(f"{name},您好,您存款{num}元成功")
    print(f"{name},您好,您的余额剩余: {money}\n")


def atm_money(name):  # 取款函数
    num = int(input("取款: "))
    global money
    money -= num
    print(f"{name},您好,您取款{num}元成功")
    print(f"{name},您好,您的余额剩余: {money}\n")


def Exit():
    print("程序退出了,欢迎下次使用")
    exit


def menu(name):  # 主菜单
    print("主菜单:")
    print(f"{name}您好,欢迎来到黑马银行ATM,请选择操作: ")
    print("查询余额 1")
    print("存款 2")
    print("取款 3")
    print("退出 4")
    select = int(input("请输入您的选择: "))
    if select == 1:
        check_money(name)
        menu(name)
    elif select == 2:
        save_money(name)
        menu(name)
    elif select == 3:
        atm_money(name)
        menu(name)
    else:
        Exit()


name = input("请输入您的名字: ")
menu(name)
