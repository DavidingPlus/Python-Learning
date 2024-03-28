# 写入文件 不存在的文件
with open("/mnt/d/Code/Python/Bilibili/文件操作/test.txt", "w", encoding="UTF-8") as file:
    file.write("hello world!")  # 内容写入到内存中 需要flush刷新才能写入到硬盘中
    file.flush()  # close()功能内置了flush功能,所以这一行可有可无!!!!

# 文件不存在会把文件创建出来 文件存在会将原有内容全部清空重新写入!!!!

with open("/mnt/d/Code/Python/Bilibili/文件操作/test.txt", "w", encoding="UTF-8") as file:
    file.write("黑马程序员")
