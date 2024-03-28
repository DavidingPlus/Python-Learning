money = 10000

for x in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{x},绩效分{score}低于5,不发工资.")
        continue
    if money == 0:
        print("工资发完了,结束发工资")
        break
    money -= 1000
    print(f"员工{x},领取工资1000元,工资剩余{money}")
