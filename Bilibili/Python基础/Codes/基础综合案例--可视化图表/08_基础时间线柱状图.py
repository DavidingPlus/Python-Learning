from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
# bar1
bar1 = Bar()
# 添加x轴和y轴
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转xy轴
bar1.reversal_axis()

# bar2
bar2 = Bar()
# 添加x轴和y轴
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
# 反转xy轴
bar2.reversal_axis()

# bar1
bar3 = Bar()
# 添加x轴和y轴
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
# 反转xy轴
bar3.reversal_axis()

# 构建时间线对象 # 主题设置
timeline = Timeline({"theme": ThemeType.LIGHT})
# 在时间线上添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,  # 自动播放时间间隔 单位毫秒
    is_timeline_show=True,  # 播放时是否显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环播放
)

# 绘图 用时间线对象绘图
timeline.render("D:\\Code\\Python\\Bilibili\\基础综合案例--可视化图表\\基础时间线柱状图.html")
