import os


def test_os():
    # 列出路径下的内容
    print(os.listdir("/mnt/d/Code/Python/Bilibili/Python高阶技巧/test"))
    # 判断指定路径是不是文件夹
    print(os.path.isdir("/mnt/d/Code/Python/Bilibili/Python高阶技巧/test/a"))
    # 判断指定路径是否存在
    print(os.path.exists("/mnt/d/Code/Python/Bilibili/Python高阶技巧/test"))


def get_file_recursion_from_dir(path) -> list:
    # 从指定的文件夹中使用递归的方式获取全部的文件列表
    file_list = list()
    if os.path.exists(path):
        for f in os.listdir(path):
            # 如果是文件就收集起来,文件夹就继续递归
            newpath = path+"/"+f
            if os.path.isdir(newpath):
                file_list += get_file_recursion_from_dir(newpath)
            else:
                file_list.append(newpath)
    else:
        print(f"指定的目录{path},不存在")
        return list()

    return file_list


if __name__ == "__main__":
    # test_os()
    print(get_file_recursion_from_dir(
        "/mnt/d/Code/Python/Bilibili/Python高阶技巧/test"))
