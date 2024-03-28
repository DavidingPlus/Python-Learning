# 捕获异常
# 捕获常规异常
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
try:
    file = open("/mnt/d/Code/Python/Bilibili/异常,模块,包/abc.txt",
                "r", encoding="UTF-8")
except:
    print("出现异常了,因为文件不存在,我将以open的模式,改为w模式去打开")
    file = open("/mnt/d/Code/Python/Bilibili/异常,模块,包/abc.txt",
                "w", encoding="UTF-8")

# 捕获指定异常
try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    # print(1/0)
    print(name)
except (NameError, ZeroDivisionError)as e:
    print("出现了变量未定义 或者 除以0的异常错误")
    print(e)
# 未正确设置捕获异常类型将无法捕获异常

# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print("出现异常了")
    print(e)

# 异常else else表示的是没有异常要执行的代码!!!
try:
    file = open("/mnt/d/Code/Python/Bilibili/异常,模块,包/abc.txt",
                "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
else:
    print("好高兴,没有异常")
finally:
    file.close()
