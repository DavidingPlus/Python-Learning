# flatMap方法
from pyspark import SparkConf, SparkContext
# 手动让spark识别到python解释器
import os
os.environ['PYSPARK_PYTHON'] = "D:\\Python\\python.exe"


conf = SparkConf().setSparkHome("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(
    ["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求,将RDD数据里面的一个个单词提取出来
# flatMap 解除嵌套,在这里让所有的字符串在一个列表里面
rdd2 = rdd.flatMap(lambda element: element.split(" "))
print(rdd2.collect())

sc.stop()
