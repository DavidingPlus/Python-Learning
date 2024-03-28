# 设计一个类,完成对学生信息的键盘输入
# 并输出为文件(txt)
import json


class Student:
    stu_list = list()  # 这个列表里面存的是每一位学生的信息,每一位学生的信息是字典

    def Input_stu(self, name, age, addr):
        # 准备一个字典模板
        model_dict = {
            "姓名": None,
            "年龄": None,
            "地址": None
        }
        model_dict["姓名"] = name
        model_dict["年龄"] = age
        model_dict["地址"] = addr
        # 将该学生信息插入到列表中
        self.stu_list.append(model_dict)

    def Show_Info(self):
        print(self.stu_list)

    def Menu(self):
        while True:
            select = int(input("请选择:\n1.录入学生信息.\n2.退出.\n"))
            if select == 1:
                name = input("请输入学生姓名: ")
                age = int(input("请输入学生年龄: "))
                addr = input("请输入学生地址: ")
                self.Input_stu(name, age, addr)
                print('\n')
                continue
            elif select == 2:
                with open("Stu_Info.txt",  # 默认路径是在本文件夹中
                          "a", encoding="UTF-8") as file:
                    # 这是个列表 并且里面的每个元素都是字典 所以将其转换为json字符串格式
                    json_str = json.dumps(self.stu_list, ensure_ascii=False)
                    file.write(json_str)
                self.Show_Info()
                print("录入信息成功,欢迎下次使用\n")
                break
            else:
                print("输入错误,请重新输入\n")
                continue


stu = Student()
stu.Menu()
