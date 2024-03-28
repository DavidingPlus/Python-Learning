# 函数 str_reserse(s) 接受字符串将其反转
def str_reserse(str):
    return str[::-1]


if __name__ == "__main__":
    print(str_reserse("hello"))


# 函数 substr(s,x,y) 按照x,y对字符串进行切片 返回x到y的值
def substr(str, x, y):
    return str[x:y]


if __name__ == "__main__":
    print(substr("  hello  ", 2, 7))
