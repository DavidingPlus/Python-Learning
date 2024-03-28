from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# # RDD对象 spark的内置数据对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

# # 如果要查看rdd里面有什么内容,需要用collect()
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 字符串会被拆分为出一个个的字符,存入rdd对象
# 字典仅有key会被存入rdd对象

# 读取文件
rdd = sc.textFile("D:\\Code\\Python\\Bilibili\\PySpark\\hello.txt")
print(rdd.collect())

sc.stop()
