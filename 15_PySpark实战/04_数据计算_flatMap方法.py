"""
演示RDD的flatMap成员方法的使用
"""
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["hello world 123", "hello hello world", "nice hello"])

# 需求，将RDD数据里面的一个个单词提取出来
# rdd2 = rdd.map(lambda x: x.split(" ")) # [['hello', 'world', '123'], ['hello', 'hello', 'world'], ['nice', 'hello']]
rdd2 = rdd.flatMap(lambda x: x.split(" ")) # ['hello', 'world', '123', 'hello', 'hello', 'world', 'nice', 'hello']
print(rdd2.collect())
