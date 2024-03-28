# 统计文件中单词出现的数量
# 1.构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 2.读取数据文件
rdd = sc.textFile("D:\\Code\\Python\\Bilibili\\PySpark\\03_数据计算\\hello.txt")
# 3.取出全部单词
word_rdd = rdd.flatMap(lambda element: element.split(" "))
# 4.将所有单词都转换为二元元组,单词为Key,value设置为1 后面根据单词分组将value相加则可以得到单词出现的数量!!!
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 5.分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a+b)
print(result_rdd)
