import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
file = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\地图数据\\疫情.txt",
            "r", encoding="UTF-8")
data = file.read()
# 关闭文件
file.close()

# 将json转换为python字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]

# 得到省份和确诊人数 组装成元组
data_list = list()  # 绘图需要用的列表
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# print(data_list)

# 创建地图对象
map = Map()
map.add("各省份确诊人数", data_list, "china")
# 设置全局数据
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 909, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000,  "label": "100000+", "color": "#990033"}
        ]
    )
)
map.render("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\全国疫情地图.html")
