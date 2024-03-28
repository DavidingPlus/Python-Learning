# rdd转换为python对象
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/phthon.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# collect算子
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子 对rdd的全部数据进行两两聚合,不进行分类!!!
num = rdd.reduce(lambda a, b: a+b)
print(num)

# take算子 取出rdd的前n个算子 返回为list
take_list = rdd.take(3)
print(take_list)

# count算子 计算rdd内有多少个元素
num_count = rdd.count()
print(num_count)

sc.stop()
