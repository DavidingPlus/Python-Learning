from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/phthon.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# saveAsTextFile算子
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([("hello", 3), ("spark", 5), ("Hi", 7)])
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]])

rdd1.saveAsTextFile(
    "D:\\Code\\Python\\Bilibili\\PySpark\\04_数据输出\\output1")
rdd2.saveAsTextFile(
    "D:\\Code\\Python\\Bilibili\\PySpark\\04_数据输出\\output2")
rdd3.saveAsTextFile(
    "D:\\Code\\Python\\Bilibili\\PySpark\\04_数据输出\\output3")
