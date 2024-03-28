# 函数 print_file_info(file_name)
# 接受路径,打印文件的全部内容,如果文件不存在则捕获异常,输出异常信息,通过finally关闭对象
def print_file_info(pathname):
    try:
        file = open(pathname, "r", encoding="UTF-8")
    except FileNotFoundError as e:
        print(f"文件不存在,异常信息是: {e}")
    else:
        mylist = file.readlines()
        print(mylist)
    finally:
        file.close()

# 函数 append_to_file(file_name,data) 接受文件路径传入数据,将数据追加到文件中


def append_to_file(pathname, data):
    with open(pathname, "a", encoding="UTF-8")as file:
        file.write(data)
