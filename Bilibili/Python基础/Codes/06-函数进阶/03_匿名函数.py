# 函数作为函数的参数
# 这是一种计算逻辑的传递 而非数据的传递
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x+y


test_func(compute)
