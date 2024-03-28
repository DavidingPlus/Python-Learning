count = 0
nopos = -1

with open("/mnt/d/Code/Python/Bilibili/文件操作/word.txt",
          "r", encoding="UTF-8") as file:
    for line in file:
        if line.find("itheima") != nopos:  # 返回-1表示没找到
            count += 1

print(f"itheima出现的次数是: {count}")
