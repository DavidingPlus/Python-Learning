# 函数嵌套的前提下,内部函数使用了外部函数的变量,
# 并且外部函数返回了内部函数,
# 则这个使用外部函数变量的内部函数叫做闭包

# 简单的闭包 为了避免全局变量被篡改的风险!!!
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")

#     return inner


# fn1 = outer("黑马程序员")
# fn1("大家好")

# 修改外部函数变量的值 加上nonlocal关键字才能在内部函数中修改外部函数的变量!!!!
# def outer(num1):
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner


# fn = outer(10)
# fn(10)
# fn(10)


# atm存钱取钱
def account_create(initial_account=0):
    def atm(num, deposit=True):
        nonlocal initial_account
        if deposit:
            initial_account += num
            print(f"存款,当前余额: {initial_account}")
        else:
            initial_account -= num
            print(f"取款,当前余额: {initial_account}")
    return atm


# 使用闭包就不用依赖外部的全局变量,消除了全局变量可能被篡改的风险
atm = account_create()
atm(100)
atm(200)
atm(100, deposit=False)
