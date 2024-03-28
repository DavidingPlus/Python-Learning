from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
import json
# 处理数据
file_us = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\折线图数据\\美国.txt",
               "r", encoding="UTF-8")
us_data = file_us.read()  # 美国

file_jp = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\折线图数据\\日本.txt",
               "r", encoding="UTF-8")
jp_data = file_jp.read()  # 日本

file_in = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\折线图数据\\印度.txt",
               "r", encoding="UTF-8")
in_data = file_in.read()  # 印度

# 去除不合json规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 处理结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 转换
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取日期数据用于x轴 到314下标结束
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]
# print(x_data)

# 获取确认数据用于y轴
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]
# print(y_data)

# 生成图表
line = Line()  # 构建折线图对象
line.add_xaxis(us_x_data)  # x轴是通用的用一个国家的即可
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
                     )

line.render("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\main.html")

# 关闭文件对象
file_us.close()
file_jp.close()
file_in.close()
