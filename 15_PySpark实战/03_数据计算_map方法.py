"""
演示RDD的map成员方法的使用
"""
import os
from pyspark import SparkConf, SparkContext

# os.environ['PYSPARK_PYTHON'] = "/home/codespace/.python/current/bin/python3"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 通过map方法将全部数据都乘以10
# def func(data):
#     return 10 * data

# rdd2 = rdd.map(func)
rdd2 = rdd.map(lambda x: x * 10)

print(rdd2.collect())
sc.stop()
