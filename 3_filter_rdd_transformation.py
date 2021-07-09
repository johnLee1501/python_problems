import logging
import os, sys

from glob2 import glob
from pyspark.sql import SparkSession

# try:
#     spark_home = os.environ['SPARK_HOME']
#
#     sys.path.append(os.path.join(spark_home, 'python'))
#     py4j_src_zip = glob(os.path.join(spark_home, 'python',
#                                      'lib', 'py4j-*-src.zip'))
#     if len(py4j_src_zip) == 0:
#         raise ValueError('py4j source archive not found in %s'
#                          % os.path.join(spark_home, 'python', 'lib'))
#     else:
#         py4j_src_zip = sorted(py4j_src_zip)[::-1]
#         sys.path.append(py4j_src_zip[0])
# except KeyError:
#     logging.error("""SPARK_HOME was not set. please set it. e.g.
#       SPARK_HOME='/home/...' ./bin/pyspark [program]""")
#     exit(-1)
# except ValueError as e:
#     logging.error(str(e))
#     exit(-1)

spark = SparkSession.builder.appName('Simple Spark Session').master('local[*]').enableHiveSupport().getOrCreate()

py_list = [1, 2, 3, 4, 5]
number_rdd = spark.sparkContext.parallelize(py_list, 3)
print(type(number_rdd))
print(number_rdd.collect())
number_even_rdd = number_rdd.filter(lambda n: n % 2 == 0)
print(number_even_rdd.collect())

py_list = ['John', 'Didier', 'Kelly']
names_rdd = spark.sparkContext.parallelize(py_list, 2)
print(type(names_rdd))
print(names_rdd.collect())
names_rdd_r = names_rdd.filter(lambda name: 'r' in name)
print(names_rdd_r.collect())

input_file_path = "./data/train.csv"
train_rdd = spark.sparkContext.textFile(input_file_path)
pass
spark.stop()
