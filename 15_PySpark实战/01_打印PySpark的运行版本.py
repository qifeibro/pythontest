"""
演示获取PySpark的执行环境入口对象: SparkContext
并通过SparkContext 对象获取当前PySpark的版本
"""
from pyspark import SparkConf, SparkContext

# 通过链式调用的方式，创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行(停止PySpark程序)
sc.stop()
