# 将python.txt进行备份并保存为新文件bill.txt
mylist = list()
nopos = -1

with open("/mnt/d/Code/Python/Bilibili/文件操作/python.txt",
          "r", encoding="UTF-8")as file:
    mylist = file.readlines()

with open("/mnt/d/Code/Python/Bilibili/文件操作/bill.txt",
          "w", encoding="UTF-8")as file:
    for line in mylist:
        file.write(line)
