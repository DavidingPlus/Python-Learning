# 函数返回多个值 通过逗号返回分隔多个值
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)
