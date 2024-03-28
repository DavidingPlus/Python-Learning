from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
# bar
bar = Bar()
# 添加x轴和y轴
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转xy轴
bar.reversal_axis()
# 绘图
bar.render("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\基础柱状图.html")
