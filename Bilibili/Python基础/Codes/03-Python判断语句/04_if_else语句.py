"""
演示练习题:成年人判断
"""

# 获取键盘输入
print("欢迎来到游乐场,成人收费,未成年免费")
age = int(input("请输入您的年龄: "))

# 通过if判断是否是成年人
if age >= 18:
    print("您已成年,需要买票10元.")
else:
    print("您未成年,可以免费游玩.")
