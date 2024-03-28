from pyspark import SparkConf, SparkContext
import json
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# TODO 需求1 : 城市销售额排名
# 读取文件
file_rdd = sc.textFile(
    "D:\\Code\\Python\\Bilibili\\PySpark\\03_数据计算\\order.txt")
json_str_rdd = file_rdd.flatMap(lambda elem: elem.split("|"))
# 将json格式转化为字符串
dict_rdd = json_str_rdd.map(lambda elem: json.loads(elem))
# (城市,销售额)
city_with_money_rdd = dict_rdd.map(lambda elem: (
    elem["areaName"], int(elem["money"])))
# 销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a+b)
# 排序
result1_rdd = city_result_rdd.sortBy(
    lambda elem: elem[1], ascending=False, numPartitions=1)
print(result1_rdd.collect())

# TODO 需求2 : 全部城市有哪些商品类别在售卖
category_rdd = dict_rdd.map(lambda elem: elem["category"]).distinct()
print(category_rdd.collect())

# TODO 需求3:北京市有哪些商品类别在售卖
beijing_data_rdd = dict_rdd.filter(lambda elem: elem["areaName"] == "北京")
beijing_category_rdd = dict_rdd.map(lambda elem: elem["category"]).distinct()
print(beijing_category_rdd.collect())
