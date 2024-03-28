from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
file = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\动态柱状图数据\\1960-2019全球GDP数据.csv",
            "r", encoding="GB2312")
data_lines = file.readlines()
# 关闭文件
file.close()
# 删除第一条数据
data_lines.pop(0)
# print(data_lines)

# 将数据转换为字典形式 {年份: [[国家,gdp],……]}
data_dict = dict()
for line in data_lines:
    year = int(line.split(",")[0])  # 将年份分离出来
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])  # 用float强制将科学计数法转换为正常的数字!!
    # 如何判断字典里有没有指定的key呢? 根据报异常来处理
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = list()
        data_dict[year].append([country, gdp])
# print(data_dict)

# 添加时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())  # 将所有的key取出来并排序
for year in sorted_year_list:  # 不直接遍历字典,因为可能数据的原因不是按顺序来的
    # 按照gdp进行降序排序 取前八
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出前八
    year_data = data_dict[year][:8][::-1]  # 按照实际要求将数据反转一下
    x_data = list()
    y_data = list()
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    # 构建树状图对象
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x y轴
    bar.reversal_axis()
    # 设置每一年图标的标题
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前八的GDP数据"))
    # 添加到时间线中去
    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 导出
timeline.render(
    "D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\1960-2019全球GDP前八国家.html")
