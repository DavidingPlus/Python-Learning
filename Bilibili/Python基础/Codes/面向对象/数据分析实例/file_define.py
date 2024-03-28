"""
和文件相关的类定义
"""
import json
from data_define import Record


# 定义一个抽象类做顶层设计,确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        # 读取文件数据,将读到的数据都转换为Record对象,将让他们都封装到list内返回即可
        pass


class TextFileReader(FileReader):
    def __init__(self, path) -> None:
        self.path = path  # 定义成员变量记录文件路径

    # 实现父类的抽象方法
    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding="UTF-8")
        record_list: list[record] = list()
        for line in file.readlines():
            line = line[:-1]  # 将每行后的回车处理掉
            # print(line)
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1],
                            int(data_list[2]), data_list[3])
            record_list.append(record)

        file.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path) -> None:
        self.path = path  # 定义成员变量记录文件路径

    def read_data(self) -> list[Record]:
        file = open(self.path, "r", encoding="UTF-8")
        record_list: list[record] = list()
        for line in file.readlines():
            line = line[:-1]
            # print(line)
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(
                data_dict["money"]), data_dict["province"])
            record_list.append(record)

        file.close()
        return record_list


if __name__ == "__main__":
    text_file_reader = TextFileReader(
        "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年1月销售数据.txt")
    json_file_reader = JsonFileReader(
        "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
