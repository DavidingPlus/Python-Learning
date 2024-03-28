# map算子
from pyspark import SparkConf, SparkContext
# 手动让spark识别到python解释器
import os
os.environ['PYSPARK_PYTHON'] = "D:\\Python\\python.exe"


conf = SparkConf().setSparkHome("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# def func(data):
#     return data * 10

# 通过map方法将全部数据乘以10 map方法:将每一条元素拿出来进行处理!!!
# 将rdd里面的每一个数据进行func函数的处理
# 链式调用 每一个map的返回对象都是rdd则链式调用
rdd2 = rdd.map(lambda element: 10 * element).map(lambda element: element+5)
print(rdd2.collect())

sc.stop()
