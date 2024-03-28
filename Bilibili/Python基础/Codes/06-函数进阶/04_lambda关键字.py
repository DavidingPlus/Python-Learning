# lambda 传入参数: 函数体(一行代码)
# lambda是关键字 表示定义匿名函数

def test_func(compute):
    result = compute(1, 2)
    print(f"结果是: {result}")


test_func(lambda x, y: x+y)  # 这是compute的匿名函数
