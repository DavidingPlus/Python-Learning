import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
file = open("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\可视化案例数据\\地图数据\\疫情.txt",
            "r", encoding="UTF-8")
data = file.read()
# 关闭文件
file.close()

# 获取河南省数据
data_dict = json.loads(data)
HENAN_cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 准备元组
data_list = list()
for city_data in HENAN_cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市数据
data_list.append(("济源市", 5))

# print(data_list)

# 构建地图
map = Map()
map.add("河南省疫情分布", data_list, "河南")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
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
map.render("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\河南省疫情地图.html")
