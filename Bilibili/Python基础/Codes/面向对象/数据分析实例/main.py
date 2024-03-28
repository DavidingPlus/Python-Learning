# 1.设计一个类,完成数据的封装
# 2.设计一个抽象类,定义文件读取的相关功能,并使用子类实现具体功能
# 3.读取文件,产生数据对象
# 4.进行数据需求的逻辑运算
# 5.通过pyecharts进行图形绘制

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader(
    "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader(
    "D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\2011年2月销售数据JSON.txt")

Jan_data: list[Record] = text_file_reader.read_data()
Feb_data: list[Record] = json_file_reader.read_data()
# 将两个月份的数据合并为个list来存储
all_data: list[Record] = Jan_data+Feb_data

# 数据计算
# {"2011-01-01":1234,……}
data_dict = dict()
for record in all_data:
    try:  # 如果key不存在就新创建一个key并且赋初值
        data_dict[record.date] += record.money
    except KeyError:
        data_dict[record.date] = record.money

# print(data_dict)

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()),
              label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("D:\\Code\\Python\\Bilibili\\面向对象\\数据分析实例\\每日销售额柱状图.html")
