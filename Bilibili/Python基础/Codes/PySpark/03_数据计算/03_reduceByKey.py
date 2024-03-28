# rdd存储的数据是 二元元组,则可称作V型RDD
# reducrByKey 将二元元组里的一组(两个)数据进行处理,根据第一个元素进行分组,第二个元素进行处理,返回一个值,填回该位置
from pyspark import SparkConf, SparkContext
# 手动让spark识别到python解释器
import os
os.environ['PYSPARK_PYTHON'] = "D:\\Python\\python.exe"


conf = SparkConf().setSparkHome("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([("男", 99), ("男", 88), ("女", 99), ("女", 66)])
# 求男生和女生两个组的乘成绩之和
rdd2 = rdd.reduceByKey(lambda a, b:  a+b)
print(rdd2.collect())  # [("男",187),("女",165)]

sc.stop()
