ret1 = range(10)  # 从 0开始到10不包含10 0 1 2 3 4 5 6 7 8 9
# print(ret1)
for x in range(10):
    print(x)
print('\n')

ret2 = range(5, 10)  # 从5开始到10 不包含10 5 6 7 8 9、
for x in range(5, 10):
    print(x)
print('\n')

ret3 = range(5, 10, 2)  # 2 步长 5 7 9
for x in range(5, 10, 2):
    print(x)

# i = 1
# while i <= 10:
#     print("送玫瑰花")
#     i += 1

for x in range(10):
    print("送玫瑰花")
