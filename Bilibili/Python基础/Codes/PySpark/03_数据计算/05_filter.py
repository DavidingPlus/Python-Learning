# Filter方法 将数据进行过滤进行保留
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
# 过滤 偶数保留
rdd2 = rdd.filter(lambda element: element % 2 == 0)  # 后面必须返回一个bool值!!!
print(rdd2.collect())
