# 1.设计一个类,完成数据的封装
# 2.设计一个抽象类,定义文件读取的相关功能,并使用子类实现具体功能
# 3.读取文件,产生数据对象
# 4.进行数据需求的逻辑运算
# 5.通过pyecharts进行图形绘制

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader(
    "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader(
    "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年2月销售数据JSON.txt")

Jan_data: list[Record] = text_file_reader.read_data()
Feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为个list来存储
all_data: list[Record] = Jan_data + Feb_data
# print(all_data)

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="05121428",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
        f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # print(sql)
    # 执行SQL语句
    cursor.execute(sql)

# 关闭MySQL链接对象
conn.close()
