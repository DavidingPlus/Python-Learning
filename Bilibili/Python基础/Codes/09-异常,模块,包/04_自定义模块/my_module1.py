def test_a(a, b):
    return a+b


def test_b(a, b):
    return a-b


# __all__ 变量
# 如果一个模块文件中有"__all__"变量,当使用 from xxx import * 导入时,只能导入这个列表中的元素!!!
__all__ = ["test_a"]

# __main__ 变量 不让其他模块的变量在导入的时候执行这一段代码,但是又想保存这一段代码方便这一块的测试
if __name__ == "__main__":
    print(test_a(1, 2))
