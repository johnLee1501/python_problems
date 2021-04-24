import os
import sys

spark_path = r"C:\Spark\spark-3.0.2-bin-hadoop2.7"  # spark installed folder
os.environ['SPARK_HOME'] = spark_path
sys.path.insert(0, spark_path + "/bin")
sys.path.insert(0, spark_path + "/python/pyspark/")
sys.path.insert(0, spark_path + "/python/lib/pyspark.zip")
sys.path.insert(0, spark_path + "/python/lib/py4j-0.10.9-src.zip")
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession

spark = SparkSession.builder \
    .appName('SparkCassandraApp') \
    .config('spark.cassandra.connection.host', 'localhost') \
    .config('spark.cassandra.connection.port', '9042') \
    .master('local[2]') \
    .getOrCreate()
df = spark.read.format("org.apache.spark.sql.cassandra").options(table="prices", keyspace="pricepred").load()
pass
# spark = SparkSession.builder \
#     .appName('SparkCassandraApp') \
#     .config('spark.cassandra.connection.host', 'localhost') \
#     .config('spark.cassandra.connection.port', '9042') \
#     .config('spark.cassandra.output.consistency.level', 'ONE') \
#     .master('local[2]') \
#     .getOrCreate()
#
# sqlContext = SQLContext(spark)
# ds = sqlContext \
#     .read \
#     .format('org.apache.spark.sql.cassandra') \
#     .options(table='prices', keyspace='pricepred') \
#     .load()

# ds.show(10)
